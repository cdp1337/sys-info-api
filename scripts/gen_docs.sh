#!/bin/bash
#
# Generate documentation for the project with lazydocs

if ! which lazydocs > /dev/null; then
	pip install lazydocs
fi

if [ ! -d "src/" ]; then
	echo "ERROR: Please run this script from the project root! (no src/ directory found)"
	exit 1
fi

if [ ! -d "docs/" ]; then
	echo "ERROR: Please run this script from the project root! (no docs/ directory found)"
	exit 1
fi

# Run the actual binary to generate documentation from source code
lazydocs src --overview-file=api.md


# Generate coverage of tests across different operating systems
echo '# OS Coverage' > docs/os_coverage.md
echo '' >> docs/os_coverage.md
echo '| Type | Collector | Test Case Coverage |' >> docs/os_coverage.md
echo '|------|-----------|--------------------|' >> docs/os_coverage.md

egrep -r '^class [^_]' src/sys_info_api/collectors/ | grep -v 'Test' | sort | while read line; do
	# Trim filename out of src/sys_info_api/collectors/bin/pkg.py:class PkgListInstalled(BinCollector):
	FILE_PATH=$(echo $line | cut -d ':' -f 1)
	# Trim class name out of src/sys_info_api/collectors/bin/pkg.py:class PkgListInstalled(BinCollector):
	CLASS_NAME=$(echo $line | cut -d ':' -f 2 | cut -d ' ' -f 2 | cut -d '(' -f 1)
	CLASS_NAME_LOWER=$(echo "$CLASS_NAME" | tr '[:upper:]' '[:lower:]')
	# Trim collector type out of src/sys_info_api/collectors/bin/pkg.py
	COLLECTOR_TYPE=$(echo "$FILE_PATH" | cut -d '/' -f 4)
	# Transform path to Python module path
	MODULE_PATH=$(echo "${FILE_PATH:4:-3}" | tr '/' '.')
	# | bin    | [AptInstall](docs/sys_info_api.collectors.bin.apt.md#class-aptinstall) | [img] [img] [img] |
	echo -n "| $COLLECTOR_TYPE | [$CLASS_NAME]($MODULE_PATH.md#class-$CLASS_NAME_LOWER) | " >> docs/os_coverage.md

	# Find the operating systems with a valid test for this class
	LAST_DISTRO=""
	for DISTRO_AND_VERSION in $(find tests/data/ -name "$COLLECTOR_TYPE.$CLASS_NAME_LOWER*.yaml" | cut -d '/' -f 3 | cut -d '-' -f 1,2 | uniq | sort); do
		DISTRO_NAME=$(echo $DISTRO_AND_VERSION | cut -d '-' -f 1)
		DISTRO_VERSION=$(echo $DISTRO_AND_VERSION | cut -d '-' -f 2)
		if [ "$DISTRO_NAME" != "$LAST_DISTRO" ]; then
			# Different distro, (group them together), render the image for this distro
			echo -n "{%img_$DISTRO_NAME%} " >> docs/os_coverage.md
			LAST_DISTRO="$DISTRO_NAME"
		fi
		# Write the version of the distro
		echo -n "$DISTRO_VERSION " >> docs/os_coverage.md
	done

	# Close the line
	echo "|" >> docs/os_coverage.md
done


# Perform auto replacements so we don't have to have crazy markdown everywhere in the code
find docs/ -name '*.md' | while read file; do
	# Operating systems
	sed -i "$file" -e 's:{%img_debian%}:![Debian](images/icons/debian.svg):g'
	sed -i "$file" -e 's:{%img_fedora%}:![Fedora](images/icons/fedora.svg):g'
	sed -i "$file" -e 's:{%img_freebsd%}:![FreeBSD](images/icons/freebsd.svg):g'
	sed -i "$file" -e 's:{%img_macos%}:![MacOS](images/icons/macos.svg):g'
	sed -i "$file" -e 's:{%img_redhat%}:![Redhat](images/icons/redhat.svg):g'
	sed -i "$file" -e 's:{%img_rocky%}:![Rocky](images/icons/rocky.svg):g'
	sed -i "$file" -e 's:{%img_ubuntu%}:![Ubuntu](images/icons/ubuntu.svg):g'

	# OS Groups

	sed -i "$file" -e 's:{%img_linux_all%}:![Debian](images/icons/debian.svg) ![Fedora](images/icons/fedora.svg) ![Redhat](images/icons/redhat.svg) ![Rocky](images/icons/rocky.svg) ![Ubuntu](images/icons/ubuntu.svg):g'

	# Appliances
	sed -i "$file" -e 's:{%img_proxmox%}:![Ubuntu](images/icons/proxmox.svg):g'
	sed -i "$file" -e 's:{%img_truenas%}:![Ubuntu](images/icons/truenas.svg):g'

	# Tweak resulting markdown to fix some issues
	sed -i "$file" -e 's:# <kbd>module</kbd>:# <kbd>module\:</kbd>:g'
	sed -i "$file" -e 's:## <kbd>class</kbd>:## <kbd>class\:</kbd>:g'
	sed -i "$file" -e 's:### <kbd>method</kbd>:### <kbd>method\:</kbd>:g'
done
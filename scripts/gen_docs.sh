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
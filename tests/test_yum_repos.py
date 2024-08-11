#  Copyright (c) 2024 Charlie Powell <cdp1337@veraciousnetwork.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, version 3.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from unittest import TestCase

from sys_info_api.collectors.etc.yum_repos import YumRepos, _YumRepo


class YumReposTest(TestCase):
	def test_enable_disable(self):
		raw = '''# This is a test repo

[extras]
name=Rocky Linux $releasever - Extras
mirrorlist=https://mirrors.rockylinux.org/mirrorlist?arch=$basearch&repo=extras-$releasever$rltype
#baseurl=http://dl.rockylinux.org/$contentdir/$releasever/extras/$basearch/os/
gpgcheck=1
enabled=1
countme=1
metadata_expire=6h
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-9
'''
		collector = YumRepos('test')
		collector.raw = raw
		self.assertTrue(collector.has_repo('extras'))
		repo = collector.get_repo('extras')
		self.assertIsInstance(repo, _YumRepo)
		self.assertFalse(repo.is_key_enabled('baseurl'))
		self.assertTrue(repo.is_key_enabled('mirrorlist'))
		repo.key_enable('baseurl')
		repo.key_disable('mirrorlist')
		self.assertTrue(repo.is_key_enabled('baseurl'))
		self.assertFalse(repo.is_key_enabled('mirrorlist'))

		repo.disable()
		self.assertEqual('0', repo.get_key_value('enabled'))

		repo.enable()
		self.assertEqual('1', repo.get_key_value('enabled'))

	def test_excluded_packages(self):
		raw = '''# This is a test repo

[extras]
name=Rocky Linux $releasever - Extras
mirrorlist=https://mirrors.rockylinux.org/mirrorlist?arch=$basearch&repo=extras-$releasever$rltype
#baseurl=http://dl.rockylinux.org/$contentdir/$releasever/extras/$basearch/os/
gpgcheck=1
enabled=1
countme=1
metadata_expire=6h
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-9
'''
		collector = YumRepos('test')
		collector.raw = raw
		repo = collector.get_repo('extras')
		self.assertEqual([], repo.get_excluded_packages())

		repo.add_excluded_package('test*')
		self.assertEqual(['test*'], repo.get_excluded_packages())

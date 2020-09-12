# test_section.py
#
# the pashmak project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
#
# This file is part of pashmak.
#
# pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cati.  If not, see <https://www.gnu.org/licenses/>.
##################################################


from TestCore import TestCore

script_content = '''
mem 'before start\\n'; out ^;

goto 10;

mem 'it will not show'; out ^;

section 10;

mem 'this is end\\n'; out ^;
'''

script_content_b = '''
mem 'before start\\n'; out ^;

set $i; mem 0; copy $i;

section 10;

mem str($i); out ^;

mem $i + 1; copy $i;

mem $i < 100; gotoif 10;

mem 'after start\\n'; out ^;
'''

class test_section(TestCore):
    def run(self):
        program_data = self.run_script(script_content)
        self.assert_equals(program_data['output'] , 'before start\nthis is end\n')

        expected_output = 'before start\n'
        i = 0
        while i < 100:
            expected_output += str(i)
            i += 1
        expected_output += 'after start\n'
        program_data = self.run_script(script_content_b)
        self.assert_equals(program_data['output'] , expected_output)

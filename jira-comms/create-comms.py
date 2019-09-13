import re
the_file = open("Done this week (JIRA).csv", "r")

real_file = the_file.read()
#real_file = re.sub(',"[\s\S]+?",', ',<REPLACED>,', real_file)

in_comment = False
item = ''
info = []
all_info = []
for char in real_file:
    if char == ',':
        # We're splitting on this
        info.append(item)
        item = ''
        continue
    elif char == '\n' and not in_comment:
        info.append(item)
        item = ''
        all_info.append(info)
        info = []
        continue
    elif char == '"':
        in_comment = not in_comment

    if in_comment:
        item = "[REDACTED]"
    else:
        item += char

to_print = {}
for item in all_info:
    if item[0] == "Summary":
        continue
    line = "["+item[1]+"] - "+item[0]
    if not item[21] in to_print:
        to_print[item[21]] = {}
    if not item[3] in to_print[item[21]]:
        to_print[item[21]][item[3]] = []
    to_print[item[21]][item[3]].append(line)

for version in sorted(to_print.keys()):
    info = to_print[version]
    print version
    for ticket_type in sorted(info.keys()):
        tickets = info[ticket_type]
        print ticket_type + ":"
        for ticket in tickets:
            print ticket
    print ""

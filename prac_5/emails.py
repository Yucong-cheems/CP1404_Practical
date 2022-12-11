emails = []
for i in range(3):
    print("Enter emails:")
    s = input()
    emails.append(s)

print(emails)
n = input("Enter names:")
if n in emails:
    print('Yes')
else:
    print('No')

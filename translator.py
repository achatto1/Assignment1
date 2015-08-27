import re, sys
f = open(sys.argv[1], 'r')
o = open("output_64bit.s",'w')

string = f.read()

new_string = re.sub('%ebp','%rbp',string)
new_string = re.sub('%esp','%rsp',new_string)
new_string = re.sub('%eax','%rax',new_string)
new_string = re.sub('%ecx','%rcx',new_string)
new_string = re.sub('%esi','%rsi',new_string)
new_string = re.sub('%edi','%rdi',new_string)

o.write(new_string)

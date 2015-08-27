.text
hello:
	.string "Hello_World"
.globl main
main:
    push   %rbp
    mov    %rsp,       %rbp
    push   $hello
    call    puts
    mov    $0,         %rax
    leave
    ret

.text
hello:
	.string "Hello_World"
.globl main
main:
    push   %ebp
    mov    %esp, %ebp
    push  $hello
    call   puts
    mov    $0, %eax
    leave
    ret

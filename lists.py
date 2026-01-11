servers = ["server1", "server2", "server3"]
print(servers)

#example 2 
for server in servers:
  print("Checking:", server)

#example 3
def cout_servers(server_list):
  return len(server_list)

total = cout_servers(servers)
print("Total servers:", total)

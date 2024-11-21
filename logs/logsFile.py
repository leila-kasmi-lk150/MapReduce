from collections import defaultdict

with open("web_access.txt", "r") as f:
    data = [line.strip().split() for line in f]

def mapper(logs):
    monthCount = defaultdict(int)
    monthIpCounts = defaultdict(lambda: defaultdict(int))   
    
    for l in logs:
        ip = l[0]
        date_str = l[3]
        month = month = date_str.split('/')[1]

        monthCount[month] += 1
        monthIpCounts[month][ip] += 1

    return monthCount, monthIpCounts


def reducer(monthCount, monthIpCounts):

    print("Number of accesses per month:")
    for month, count in monthCount.items():
        print(f"{month}: {count}")

    print("\nIP address with the most accesses per month:")
    ipPerMonth = {}
    
    for month, ip_data in monthIpCounts.items():
        max_ip = max(ip_data, key=ip_data.get)  
        ipPerMonth[month] = (max_ip, ip_data[max_ip])
    
    for month, (ip, count) in ipPerMonth.items():
        print(f"{month} , {ip}, Access: {count}")


month = defaultdict(int)
monthIp = defaultdict(lambda: defaultdict(int)) 

month, monthIp = mapper(data)
reducer(month, monthIp)

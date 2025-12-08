import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://free-proxy-list.net/en/"

def get_proxies():
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    proxy_table = soup.find('table', class_='table table-striped table-bordered')
    
    proxies = []
    proxies2 = []

    for row in proxy_table.tbody.find_all('tr'):
        cols = row.find_all('td')
        ip = cols[0].text
        port = cols[1].text
        https = cols[6].text
        scheme = 'https' if https == 'yes' else 'http'
        proxy = f"{scheme}://{ip}:{port}"
        proxy2 = f"{ip}:{port}"
        proxies.append(proxy)
        proxies2.append(proxy2)
    
    with open('proxy_scheme.txt', 'w') as f:
        for proxy in proxies:
            f.write(proxy + '\n')
    
    with open('proxy.txt', 'w') as f:
        for proxy2 in proxies2:
            f.write(proxy2 + '\n')
    
    print(f"Total dengan skema: {len(proxies)} | Total tanpa skema: {len(proxies2)}")
    return proxies, proxies2

def check_single_proxy(proxy_full, proxy_simple):
    scheme = proxy_full.split('://')[0]
    proxies = {
        "http": f"{scheme}://{proxy_simple}",
        "https": f"{scheme}://{proxy_simple}"
    }
    try:
        r = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=3)
        if r.status_code == 200:
            ip = r.json()['origin']
            print(f"✅ {proxy_full}")
            return (proxy_full, proxy_simple, True)
    except Exception:
        print(f"❌ {proxy_full}")
    return (proxy_full, proxy_simple, False)

def get_active_proxies(proxy_list, proxy_list_no_scheme, max_workers=50):
    working_proxies = []
    working_proxies_no_scheme = []

    print(f"\nMengecek {len(proxy_list)} proxy dengan {max_workers} thread...\n")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(check_single_proxy, proxy_full, proxy_simple): (proxy_full, proxy_simple)
            for proxy_full, proxy_simple in zip(proxy_list, proxy_list_no_scheme)
        }
        
        for future in as_completed(futures):
            proxy_full, proxy_simple, is_working = future.result()
            if is_working:
                working_proxies.append(proxy_full)
                working_proxies_no_scheme.append(proxy_simple)

    with open('proxy_scheme_active.txt', 'w') as f:
        for proxy in working_proxies:
            f.write(proxy + '\n')
    
    with open('proxy_active.txt', 'w') as f:
        for proxy in working_proxies_no_scheme:
            f.write(proxy + '\n')

    print(f"\n✅ Proxy aktif tersimpan: {len(working_proxies)}/{len(proxy_list)}")
    return working_proxies, working_proxies_no_scheme


print("Mengambil daftar proxy...")
proxy_list, proxy_list_no_scheme = get_proxies()
get_active_proxies(proxy_list, proxy_list_no_scheme)

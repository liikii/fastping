import asyncio
import aioping


def get_hosts(fp: str):
    with open(fp, encoding='utf8') as f:
        for ln in iter(f.readline, ''):
            lnd = ln.strip()
            if lnd != '':
                yield lnd


async def do_ping(host):
    try:
        delay = await aioping.ping(host, timeout=6) * 1000
        print("%s response in %s ms" % (host, delay))
    except TimeoutError:
        print("%s Timed out" % host)
    except OSError:
        print("%s Timed out" % host)


async def f_ping(hosts):
    tasks = []
    for host in hosts:
        tasks.append(do_ping(host))
    tasks = tuple(tasks)
    await asyncio.gather(*tasks, return_exceptions=True)


loop = asyncio.get_event_loop()
loop.run_until_complete(f_ping(get_hosts('ips3.txt')))

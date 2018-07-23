# from threading import Thread
# # class InputReader(Thread):
# #     def run(self):
# #         self.line_of_text = input()
# # print("Enter some text and press enter: ")
# # thread = InputReader()
# # thread.start()
# # count = result = 1
# # while thread.is_alive():
# #     result = count * count
# #     count += 1
# # print("calculated squares up to {0} * {0} = {1}".format(count, result))
# # print("while you typed '{}'".format(thread.line_of_text))

# import json
# from urllib.request import urlopen
# import time
# CITIES = ['Edmonton','Victoria', 'Winnipeg', 'Fredericton',"St. John's", 'Halifax', 'Toronto', 'Charlottetown','Quebec City', 'Regina']
# class TempGetter(Thread):
#     def __init__(self, city):
#         super().__init__()
#         self.city = city
#     def run(self):
#         url_template = ('https://api.openweathermap.org/data/2.5/''weather?q={},CA&units=metric')
#         response = urlopen(url_template.format(self.city))
#         data = json.loads(response.read().decode())
#         self.temperature = data['main']['temp']
# threads = [TempGetter(c) for c in CITIES]
# start = time.time()
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
# for thread in threads:
#     print("it is {0.temperature:.0f}°C in {0.city}".format(thread))
# print("Got {} temps in {} seconds".format(len(threads), time.time() - start))


# from multiprocessing import Process, cpu_count
# import time
# import os
# class MuchCPU(Process):
#     def run(self):
#         print(os.getpid())
#         for X in range(200000000):
#             pass
# if __name__ == '__main__':
#     procs = [MuchCPU() for f in range(cpu_count())]
#     t = time.time()
#     for p in procs:
#         p.start()
#     for p in procs:
#         p.join()
#     print('work took {} seconds'.format(time.time() - t))



# import random
# from multiprocessing.pool import Pool
# def prime_factor(value):
#     factors = []
#     for divisor in range(2, value-1):
#         quotient, remainder = divmod(value, divisor)
#         if not remainder:
#             factors.extend(prime_factor(divisor))
#             factors.extend(prime_factor(quotient))
#             break
#         else:
#             factors = [value]
#     return factors
# if __name__ == '__main__':
#     pool = Pool()
#     to_factor = [random.randint(100000, 50000000) for i in range(20)]
#     results = pool.map(prime_factor, to_factor)
#     for value, factors in zip(to_factor, results):
#         print("The factors of {} are {}".format(value, factors))



# def search(paths, query_q, results_q):
#     lines = []
#     for path in paths:
#         lines.extend(l.strip() for l in path.open())
#     query = query_q.get()
#     while query:
#         results_q.put([l for l in lines if query in l])
#         query = query_q.get()

# if __name__ == '__main__':
#     from multiprocessing import Process, Queue, cpu_count
#     from path import path
#     cpus = cpu_count()
#     pathnames = [f for f in path('.').listdir() if f.isfile()]
#     paths = [pathnames[i::cpus] for i in range(cpus)]
#     query_queues = [Queue() for p in range(cpus)]
#     results_queue = Queue()
#     search_procs = [
#     Process(target=search, args=(p, q, results_queue))
#     for p, q in zip(paths, query_queues)]
#     for proc in search_procs: proc.start()


# import asyncio
# import random
# @asyncio.coroutine
# def random_sleep(counter):
#     delay = random.random() * 5
#     print("{} sleeps for {:.2f} seconds".format(counter, delay))
#     yield from asyncio.sleep(delay)
#     print("{} awakens".format(counter))
# @asyncio.coroutine
# def five_sleepers():
#     print("Creating five tasks")
#     tasks = [asyncio.async(random_sleep(i)) for i in range(5)]
#     print("Sleeping after starting five tasks")
#     yield from asyncio.sleep(2)
#     print("Waking and waiting for five tasks")
#     yield from asyncio.wait(tasks)
# asyncio.get_event_loop().run_until_complete(five_sleepers())
# print("Done five tasks")




import asyncio
from contextlib import suppress
ip_map = {b'facebook.com.': '173.252.120.6',b'yougov.com.': '213.52.133.246',b'wipo.int.': '193.5.93.80'}
def lookup_dns(data):
    domain = b''
    pointer, part_length = 13, data[12]
    while part_length:
        domain += data[pointer:pointer+part_length] + b'.'
        pointer += part_length + 1
        part_length = data[pointer - 1]
    ip = ip_map.get(domain, '127.0.0.1')
    return domain, ip
def create_response(data, ip):
    ba = bytearray
    packet = ba(data[:2]) + ba([129, 128]) + data[4:6] * 2
    packet += ba(4) + data[12:]
    packet += ba([192, 12, 0, 1, 0, 1, 0, 0, 0, 60, 0, 4])
    for x in ip.split('.'): 
        packet.append(int(x))
    return packet
class DNSProtocol(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        self.transport = transport
    def datagram_received(self, data, addr):
        print("Received request from {}".format(addr[0]))
        domain, ip = lookup_dns(data)
        print("Sending IP {} for {} to {}".format(domain.decode(), ip, addr[0]))
        self.transport.sendto(create_response(data, ip), addr)
loop = asyncio.get_event_loop()
transport, protocol = loop.run_until_complete(
loop.create_datagram_endpoint(DNSProtocol, local_addr=('127.0.0.1', 4343)))
print("DNS Server running")
with suppress(KeyboardInterrupt):
    loop.run_forever()
transport.close()
loop.close()


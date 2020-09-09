import urllib, json
from sys import argv


from pyfiglet import Figlet

custom_fig = Figlet(font='graffiti')

apikey = 'XXXXXXXXXXXXXXXXXXXXXXX' #set ur api
page = '100' #default in shodan 
print(custom_fig.renderText('SHODORK'))
print('\t Shodan Dork asn Generator | By https://github.com/xcapri/\n')
ip = argv[1]
readsplit = open(ip).read().splitlines()

def get_asn(ip):
	x = 'https://api.shodan.io/shodan/host/'+ ips +'?key='+ apikey +''
	response = urllib.urlopen(x)
	data = json.loads(response.read())
	if "asn" in data:
		asn = data['asn']

		print(ip+' ASN:'+asn )
		save = open('asn.txt', 'a')
		save.write(asn+'\n')
		save.close()

	return get_asn
def get_ip(asn):

    
	for pa in range(100):
		ipp = 'https://api.shodan.io/shodan/host/search?key='+ apikey +'&query=asn:'+ asn +'&page='+ str(pa) + '&facets=facets'
		ipl = urllib.urlopen(ipp)
		lip = json.loads(ipl.read())
		if 'matches' in lip:
			for pip in range(len(lip['matches'])):
			 print(lip['matches'][pip]['ip_str'])

			save = open('randomip.txt', 'a')
			save.write((lip['matches'][pip]['ip_str'])+'\n')
			save.close()
		elif 'error' in lip:
			print((lip['matches'][pip]['ip_str'])+ ' Error')
		




for ips in readsplit:

	get_asn(ips)
	readsplitt = open('asn.txt').read().splitlines()
	for red in readsplitt:
		lines=open('asn.txt', 'r').readlines()
        lines_set = set(lines)
        out=open('asnc.txt', 'w')
        for line in lines_set:
                out.write(line)
        readsplittt = open('asnc.txt').read().splitlines()
        for ipi in readsplittt:
            	get_ip(ipi)
            	readsplitttt = open('randomip.txt').read().splitlines()
            	for gip in readsplitttt:
            		lines=open('randomip.txt', 'r').readlines()
            		lines_set = set(lines)
            		out=open('goodip.txt', 'w')
            		for line in lines_set:
            			out.write(line)

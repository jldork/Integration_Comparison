import re
import requests

def get_dynatrace_integrations():
    r = requests.get("https://www.dynatrace.com/technologies/")
    DT_INTS = re.findall('symbol id=\"(.*?)\"', r.text)

    return DT_INTS

def get_signalfx_integrations():
    r = requests.get("https://www.signalfx.com/integrations/")
    results = re.findall('<h2 class=\"h2-2\">(.*?)</h2>', r.text)
    SFX_INTS = [x for x in results if "Signal" and "[New]" not in x]

    return SFX_INTS

def get_datadog_integrations():
    r = requests.get("https://docs.datadoghq.com/integrations/")
    DD_INTS = re.findall('<a class=card-img href=https://docs.datadoghq.com/integrations/(.*?)>', r.text)

    return DD_INTS

DT_INTS = get_dynatrace_integrations()
SFX_INTS = get_signalfx_integrations()
DD_INTS = get_datadog_integrations()

print("\nDYNATRACE\n========")
print("We have found {} integrations:".format(str(len(DT_INTS))))
print(DT_INTS)

print("\nSignalFX\n========")
print("We have found {} integrations:".format(str(len(SFX_INTS))))
print(SFX_INTS)


print("\nDATADOG\n========")
print("We have found {} integrations:".format(str(len(DD_INTS))))
print(DD_INTS)

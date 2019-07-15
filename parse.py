import re

''' html source from: https://www.dynatrace.com/technologies/ '''
def get_dynatrace_integrations():
    with open('./dt_integrations.html') as integrations_file:
        integrations_text = integrations_file.read()

    DT_INTS = re.findall('symbol id=\"(.*?)\"', integrations_text)
    return DT_INTS

''' html source from: https://www.signalfx.com/integrations/ '''
def get_signalfx_integrations():
    with open('./sfx_integrations.html') as integrations_file:
        integrations_text = integrations_file.read()

    results = re.findall('<h2 class=\"h2-2\">(.*?)</h2>', integrations_text)
    SFX_INTS = [x for x in results if "Signal" not in x]

    return SFX_INTS

''' html source from: https://docs.datadoghq.com/integrations '''
def get_datadog_integrations():
    with open('./dd_integrations.html') as integrations_file:
        integrations_text = integrations_file.read()
    DD_INTS = re.findall('<h4 class=\"card-title\">(.*?)</h4>', integrations_text)
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

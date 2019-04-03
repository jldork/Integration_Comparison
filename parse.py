import re

def get_dynatrace_integrations():
    with open('./dt_integrations.html') as integrations_file:
        integrations_text = integrations_file.read()

    results = re.findall("aria-label=\".*\"", integrations_text)
    DT_INTS = [tag.lstrip('aria-label=\"').rstrip(' logo\"') for tag in results]

    return DT_INTS

def get_datadog_integrations():
    with open('./dd_integrations.html') as integrations_file:
        integrations_text = integrations_file.read()

    results = re.findall("href=\"https://docs.datadoghq.com/integrations/.*\"", integrations_text)
    DD_INTS = set([tag.split('integrations/')[1].rstrip("\"") for tag in results])

    return DD_INTS
    
DT_INTS = get_dynatrace_integrations()
DD_INTS = get_datadog_integrations()

print("\nDYNATRACE\n========")
print("We have found {} integrations:".format(str(len(DT_INTS))))
print(DT_INTS)

print("\nDATADOG\n========")
print("We have found {} integrations:".format(str(len(DD_INTS))))
print(DD_INTS)
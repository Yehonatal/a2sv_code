def subdomainVisits(cpdomains):
    domain_map = {}

    for cpdomain in cpdomains:
        rep, domains = cpdomain.split()
        domains = domains.split(".")

        if len(domains) == 3:
            d1, d2, d3 = domains
        elif len(domains) == 2:
            d1, d2 = domains

    # return cpdomains
    ...


cpdomains = ["9001 discuss.leetcode.com"]
print(subdomainVisits(cpdomains))


cpdomains = ["900 google.mail.com", "50 yahoo.com",
             "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(cpdomains))

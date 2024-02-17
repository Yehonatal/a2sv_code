def subdomainVisits(cpdomains):
    domain_hash = {}

    for cpdomain in cpdomains:
        rep, domains = cpdomain.split()
        domain_hash[domains] = rep

    return domain_hash


cpdomains = ["9001 discuss.leetcode.com"]
print(subdomainVisits(cpdomains))

cpdomains = ["900 google.mail.com", "50 yahoo.com",
             "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(cpdomains))

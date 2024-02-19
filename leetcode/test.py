def subdomainVisits(cpdomains):
    domain_hash = {}

    for cpdomain in cpdomains:
        rep, domains = cpdomain.split()
        domains = domains.split(".")

        if len(domains) == 3:
            domain_hash[".".join(domains[:])] = domain_hash.get(
                ".".join(domains[:]), 0) + int(rep)
            domain_hash[".".join(domains[-2:])] = domain_hash.get(
                ".".join(domains[-2:]), 0) + int(rep)
            domain_hash[domains[-1]
                        ] = domain_hash.get(domains[-1], 0) + int(rep)
        elif len(domains) == 2:
            domain_hash[".".join(domains[:])] = domain_hash.get(
                ".".join(domains[:]), 0) + int(rep)
            domain_hash[domains[-1]
                        ] = domain_hash.get(domains[-1], 0) + int(rep)

    return [f"{val} {key}" for (key, val) in domain_hash.items()]


cpdomains = ["9001 discuss.leetcode.com"]
print(subdomainVisits(cpdomains))

cpdomains = ["900 google.mail.com", "50 yahoo.com",
             "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(cpdomains))


""" 
    # 1: Definitely not a medium problem 
        - Just have a hash map with the domain:visits key values pairs where you just 
        track the incoming domains and if the domain already exists just add the visits and
        return after creating a formatted value + key list of the sub domains 
            - There are cases where the domains could have 3 or 2 levels which I would 
            create the sub domains based on thus cases there can't just be a top level (com) so
            no need to check for that case 

    Time: O(n)
    Space: O(n)



"""

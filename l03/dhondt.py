import json

PARTIES = ["PO", "PSL", "PiS", "RPL", "SLD", "MN"]

with open("results2011.json", encoding="utf-8") as f:
    data = json.load(f)

print(" & ".join(["\tnr okręgu", "nazwa"] + PARTIES), "\\\\ \\hline")

final_results = {party: 0 for party in PARTIES}

for district in data:
    quotients = []
    mandates = int(district["Mandaty"])

    divisor = 1
    while len(quotients) < mandates * len(PARTIES):
        for party in PARTIES:
            votes_percent = district[party]
            if votes_percent > 5.0 or party == "MN":
                quotients += [(party, votes_percent / divisor)]
        divisor += 1

    results = sorted(quotients, key=lambda el: el[1], reverse=True)[:mandates]

    names = [r[0] for r in results]
    district_results = {name: names.count(name) for name in names}

    print(
        "\t", " & ".join(
            [str(district["Okreg"]), str(district["Nazwa"])]
            + [
                str(district_results.get(party, "0"))
                for party in PARTIES
            ]
        ), "\\\\ \\hline"
    )

    for party in PARTIES:
        final_results[party] += district_results.get(party, 0)

print("\t& RAZEM &", " & ".join(str(v) for v in final_results.values()), "\\\\ \\hline")
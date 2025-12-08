import random

# Generar el codi secret de 4 xifres
def generar_codi():
    codi = ""
    for _ in range(4):
        codi += str(random.randint(0, 9))
    return codi


# Comprovar encerts i coincidències
def comprovar(codi_secret, intent):
    ben_colocats = 0
    coincidencies = 0

    codi_aux = list(codi_secret)
    intent_aux = list(intent)

    # Primer: comptar els ben col·locats
    for i in range(4):
        if intent_aux[i] == codi_aux[i]:
            ben_colocats += 1
            codi_aux[i] = None
            intent_aux[i] = None

    # Després: comptar les coincidències mal col·locades
    for i in range(4):
        if intent_aux[i] in codi_aux and intent_aux[i] is not None:
            coincidencies += 1
            codi_aux[codi_aux.index(intent_aux[i])] = None

    return ben_colocats, coincidencies


# ───────── PROGRAMA PRINCIPAL ─────────

codi_secret = generar_codi()
encertat = False

print("MASTERMIND - Endevina el codi de 4 xifres")

while not encertat:
    intent = input("Introdueix un codi de 4 xifres: ")

    if len(intent) != 4 or not intent.isdigit():
        print("Has d'introduir exactament 4 números.")
        continue

    ben_colocats, coincidencies = comprovar(codi_secret, intent)

    print("Ben col·locats:", ben_colocats)
    print("Coincidències:", coincidencies)

    if ben_colocats == 4:
        print("HAS ENDEVINAT EL CODI!")
        encertat = True

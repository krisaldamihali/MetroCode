# Shembull 2. Mund të përdorim elif për të zgjeruar kushtet tona.
# Kujdes! Kushtet nuk mund te mbarojne me elif, por duhet if - elif - else.
temperature = int(input("Sa është temperatura (në gradë Celsius)? "))

if temperature >= 30:
    print("Është shumë ngrohtë. Koha për plazh!")
elif temperature >= 20:
    print("Temperaturë normale. Mund të dalësh për një shëtitje.")
elif temperature >= 10:
    print("Pak ftohtë. Kujdes me veshjen!")
elif temperature == 0:
    print("Kjo është fiks pika e ngrirjes.")
else:
    print("Është shumë ftohtë. Duhen rroba të trasha!")

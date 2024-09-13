dias = 1
horas = 3
minutos = 46
segundos = 40

total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(f"Total de segundos: {total_segundos}")

total_segundos = 87426

horas = total_segundos // 3600
resto_segundos = total_segundos % 3600

minutos = resto_segundos // 60

segundos = resto_segundos % 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos")

seg_tot = 500000

segf = seg_tot % 60
min = seg_tot // 60

minf = min % 60
hora = min // 60

horaf = hora % 24
dia = hora // 24 

print(dia, 'dia', horaf, 'hora', minf, 'min', segf, 'segf')

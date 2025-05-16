autonomia_km_por_litro = 12
tanque_litros = 40

distancia_viagem = 450
consumoviagem = tanque_litros * autonomia_km_por_litro

 
print ("Você não precisará reabastecer durante a viagem", consumoviagem >= distancia_viagem)

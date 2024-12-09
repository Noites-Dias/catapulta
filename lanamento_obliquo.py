import numpy as np

def lanca (dist_pelotao,num,angulo=45,espaco=1.5,densi=1650,temp_lanc=1, proc=20, gravidade=9.8 ):
    #dist_pelotao =distância para o pelotão em Km
    #num = numero de sodados no pelotão
    #angulo = angulo de lançamento em graus
    #espaço = espaçamento entre os soldados no pelotão em metros. Valor estimado 1,5m
    #densi = densidade da rocha utilizada em Kg/m^3. Valor estimado 1650, vlor médio da rocha marrom
    #temp_lanc = tempo estimado de lancamento em que os guerreiros aplicam a força na rocha. Valor estimado 1s
    #proc = quantos % é o raio de empacto em relação ao raio da rocha
    #gravidade = aceleração da gravidade em m/s^2

    diam = (np.sqrt(2)*(np.sqrt(num)-1)*espaco)/(1+(proc/100))  #estima o diâmetro da rocha com base no número de soldados e o raio de impacto

    
    massa = (densi*np.pi*(diam**3))/6 #define a massa da rocha com base no diâmetro

    
    angulo = (np.pi/180)*angulo    #transforma o angulo para radanos
    velo = np.sqrt((dist_pelotao*gravidade)/(2*np.cos(angulo)*np.sin(angulo)))     #define a velocidade de lancamento com base na distância no pelotão

    forca = massa*(velo/temp_lanc)  # calcula a força de lançamento com base na massa e na acelereção que ela sofreu, calculada pela velocidade nescessaria e o tempo para lançamento

    return forca,diam

resposta = lanca(int(input("Distancia ao pelotão em Km: ")),int(input("Numero estimádo de soldados no pelotão: ")))
print("Será lançada uma rocha de ",resposta[1], "m de diâmetro com " ,resposta[0], " newtons de força")

# Simulador de Lançamento de Rochas para Guerreiros Dobradores de Terra

Este programa simula o lançamento de uma rocha por guerreiros dobradores de terra do universo fictício de Avatar, calculando o tamanho e a força necessária para atingir um pelotão inimigo. O cálculo considera variáveis como o número de soldados inimigos, a distância do pelotão e propriedades físicas do lançamento.

## Funcionamento do Programa

O programa utiliza as seguintes entradas:
- **Distância do pelotão inimigo (em km):** Distância horizontal até o alvo.
- **Número de soldados no pelotão:** Utilizado para estimar o tamanho do pelotão.
- **Parâmetros adicionais (opcionais):** Espaçamento entre soldados, densidade da rocha, tempo de lançamento, proporção do raio de impacto e aceleração da gravidade.

Como saída, o programa calcula:
- **Diâmetro da rocha (em metros):** Determinado com base no tamanho do pelotão.
- **Força necessária para o lançamento (em Newtons):** Calculada a partir das propriedades físicas da rocha e da trajetória.

### Cálculos Fundamentais

1. **Estimativa do tamanho do pelotão:**
   Considera-se que os soldados se organizam em formações quadradas. O espaçamento entre soldados é definido por padrão como 1,5 metros. O tamanho do pelotão é dado por:
   
Diagonal do pelotão = sqrt(2) * ((sqrt(N) - 1) * espaçamento)

onde `N` é o número de soldados. O diâmetro da rocha é ajustado pela proporção do raio de impacto `p%` (por padrão, 20%):

Diâmetro da rocha = Diagonal do pelotão / (1 + (p / 100))

2. **Massa da rocha:**
A massa da rocha é calculada utilizando a densidade média da rocha (1.650 kg/m³) e o volume de uma esfera, considerando o diâmetro estimado:

Massa da rocha = (pi * Diâmetro^3) / 6 * Densidade

3. **Velocidade de lançamento:**
Para atingir a distância horizontal (`d`), assumimos um ângulo de lançamento de 45 graus. A velocidade necessária é calculada considerando o alcance máximo de um lançamento oblíquo:

Velocidade = sqrt((d * g) / (2 * cos(ângulo) * sin(ângulo)))

onde `g` é a aceleração da gravidade (9,8 m/s²).

4. **Força necessária:**
Por fim, a força necessária para lançar a rocha é calculada com base na segunda lei de Newton (F = m * a), considerando a aceleração como a velocidade dividida pelo tempo estimado de aplicação da força (`1 segundo`):

Força = Massa * (Velocidade / Tempo)

### Estrutura do Código

O código principal está implementado na função `lanca`, que realiza os cálculos descritos acima. As entradas do usuário são processadas para retornar o diâmetro da rocha e a força necessária.

```python
def lanca(dist_pelotao, num, angulo=45, espaco=1.5, densi=1650, temp_lanc=1, proc=20, gravidade=9.8):
 diam = (np.sqrt(2)*(np.sqrt(num)-1)*espaco)/(1+(proc/100))
 massa = (densi*np.pi*(diam**3))/6
 angulo = (np.pi/180)*angulo
 velo = np.sqrt((dist_pelotao*gravidade)/(2*np.cos(angulo)*np.sin(angulo)))
 forca = massa*(velo/temp_lanc)
 return forca, diam


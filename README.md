# Métodos Numéricos
Projeto para a disciplina de Métodos Numéricos no Centro de Informática - UFPE.
O projeto foi construído utilizando a linguagem Python. Desenvolvido pelo aluno João Rafael da Silva Faria.

### Bibliotecas utilizadas:

    1 - SymPy:  https://www.sympy.org/en/index.html 
        Utilizada para interpretar as equações diferenciais.


### Para executar, siga os passos:
    
     a) Se você for baixar o projeto através do github

        1. Clone o repositório para o seu ambiente de trabalho.
        2. Coloque as entradas no arquivo "entrada.txt".
        3. Execute o comando "python projeto.py" no prompt de comando no diretório da pasta clonada.
        4. A saída estará no arquivo "saida.txt" previamente criado ou não.
    
     b) Se você for baixar o projeto através do arquivo zipado.

        1. Baixe o arquivo .zip para seu ambiente de trabalho.
        2. Extraia o arquivo para alguma pasta.
        3. Coloque as entradas no arquivo "entrada.txt".
        4. Execute o comando "python projeto.py" no prompt de comando no diretório da pasta extraída.
        5. A saída estará no arquivo "saida.txt" previamente criado ou não.

### Funções e Formato da entrada:

    O projeto consegue calcular os seguintes métodos numéricos:

        -Euler simples:

            Sintaxe: "euler yInicial tInicial tamanhoDoPasso numPassos eqDiferencial"

        -Euler inverso

            Sintaxe: "euler_inverso yInicial tInicial tamanhoDoPasso numPassos eqDiferencial"

        -Euler aprimorado

            Sintaxe: "euler_aprimorado yInicial tInicial tamanhoDoPasso numPassos eqDiferencial"

        -Runge Kutta de 4ª ordem

            Sintaxe: "runge_kutta yInicial tInicial tamanhoDoPasso numPassos eqDiferencial"

        -Adams-Bashforth (ordens de 2 a 8)

            Sintaxes:
                "adam_bashforth nPontos  tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "adam_bashforth_by_euler yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "adam_bashforth_by_euler_inverso yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "adam_bashforth_by_euler_aprimorado yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "adam_bashforth_by_runge_kutta yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"

        -Adams-Multon (ordens de 2 a 8)

            Sintaxes:
                "adam_multon nPontos  tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "adam_multon_by_euler yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "adam_multon_by_euler_inverso yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "adam_multon_by_euler_aprimorado yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "adam_multon_by_runge_kutta yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"

        -Fórmula de Diferenciação Inversa (ordens de 2 a 6)

            Sintaxes:
                "formula_inversa nPontos  tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "formula_inversa_by_euler yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "formula_inversa_by_euler_inverso yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "formula_inversa_by_euler_aprimorado yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"
                "formula_inversa_by_runge_kutta yInicial tInicial tamanhoDoPasso numPassos eqDiferencial ordemN"

### Exemplo de entrada e saída:
        
        Entrada:
            euler 0 0 0.1 20 1-t+4*y
            runge_kutta 0 0 0.1 20 1-t+4*y
            adam_multon 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 5
            formula_inversa_by_euler 0 0 0.1 20 1-t+4*y 6
        
        Saída:
            Metodo de Euler
            y(0.0) = 0.0
            h = 0.1
            0 0.0
            1 0.100000000000000
            2 0.230000000000000
            3 0.402000000000000
            4 0.632800000000000
            5 0.945920000000000
            6 1.37428800000000
            7 1.96400320000000
            8 2.77960448000000
            9 3.91144627200000
            10 5.48602478080000
            11 7.68043469312000
            12 10.7426085703680
            13 15.0196519985152
            14 20.9975127979213
            15 29.3565179170898
            16 41.0491250839257
            17 57.4087751174960
            18 80.3022851644944
            19 112.343199230292
            20 157.190478922409

            Metodo de Runge Kutta
            y(0.0) = 0.0
            h = 0.1
            0 0.0
            1 0.117200000000000
            2 0.279737813333333
            3 0.509907554076445
            4 0.840966095334301
            5 1.32252382328002
            6 2.02858620464758
            7 3.06954966101296
            8 4.61009621432173
            9 6.89588752611087
            10 10.2933852856171
            11 15.3492526100646
            12 22.8789650935203
            13 34.0989948621741
            14 50.8239939357338
            15 75.7609392203986
            16 112.947918399709
            17 168.408681474126
            18 251.129057111003
            19 374.513505461054
            20 558.557906546437

            Metodo de Adam Multon
            y(0.0) = 0.0
            h = 0.1
            0 0.0
            1 0.1
            2 0.23
            3 0.402
            4 0.6328
            5 1.00788789037037
            6 1.56301754079324
            7 2.37362851989450
            8 3.57169407509225
            9 5.34745165336271
            10 7.98372657875157
            11 11.9041241310304
            12 17.7402749542470
            13 26.4341854643962
            14 39.3912405390358
            15 58.7079689247486
            16 87.5118939044728
            17 130.468583283445
            18 194.538019544585
            19 290.102930910325
            20 432.652015328733

            Metodo de Formula Inversa de Diferenciacao por Euler
            y(0.0) = 0.0
            h = 0.1
            0 0.0
            1 0.100000000000000
            2 0.230000000000000
            3 0.402000000000000
            4 0.632800000000000
            5 0.945920000000000
            6 1.42333067755102
            7 2.17028715532084
            8 3.28685222933592
            9 4.91951229910342
            10 7.33161599682396
            11 10.9314863555030
            12 16.3007549493079
            13 24.2906707143868
            14 36.1881057826549
            15 53.9286358440705
            16 80.3907040246658
            17 119.854893376603
            18 178.710979937451
            19 266.502400703009
            20 397.466067186996
    
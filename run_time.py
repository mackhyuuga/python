import time

# Define nosso decorator
def runtime(funcao):
    def wrapper():
        # Calcula o tempo de execução
        start_time = time.time()
        funcao()
        final_time = time.time()

        # Formata a mensagem que será mostrada na tela
        print("[{funcao}] Total run time: {total_time}".format(
            funcao=funcao.__name__,
            total_time=str(final_time - start_time))
        )

    return wrapper

# Decora a função com o decorator

# caso execute esse codigo diretamente ao invés de importar, essa parte será executada 
if __name__ == '__main__':   
    @runtime
    def main():
        for n in range(0, 100000000):
            pass

    # Executa a função main
    main()


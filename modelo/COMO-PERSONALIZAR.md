# Modelo para os próximos gerentes

Esta é a base técnica reutilizável, sem vendas ou dados de equipe incorporados. Os 24 outros gerentes são oportunidades de comercialização, ainda não vendas contratadas.

1. Copie esta pasta para um novo projeto.
2. Recolha nome, unidade, foto autorizada, preferências de tema e rotina. Prepare avatar sem fundo, retrato com fundo e imagem principal próprios.
3. Preencha `config-exemplo.json` e coloque as imagens nos caminhos definidos. O identificador deve ser exclusivo por gerente.
4. Execute `python personalizar.py config-exemplo.json --saida dist`.
5. Teste `dist/identificador/index.html` no celular e computador. Publique em um endereço próprio, e importe apenas o histórico da unidade correta.

O gerador substitui nome, empresa, imagens, cores, tarefas, hábitos e identificadores de armazenamento. O campo opcional `treinos` aceita um objeto com Segunda a Sábado, cada dia com `focus` e `exercises`.

A base conserva os módulos atuais, inclusive leitura bíblica. Preferências religiosas, novas regras de gestão, privacidade, login e sincronização devem ser alinhados com cada cliente; não prometa essas adaptações como já contratadas. Nunca inclua os dados de Vitória no material de demonstração de outro gerente.

As configurações não contêm preços. A proposta comercial deve definir implantação, personalização, suporte e eventual manutenção antes da contratação.

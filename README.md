monkeyrunner
============

Instalação
==========

- Instalar o Android SDK. O monkeyrunner já vem junto.

- Baixar o [AndroidViewClient](https://github.com/dtmilano/AndroidViewClient)

- Adicionar o ANDROID_HOME (caminho para o SDK) e ANDROID_VIEW_CLIENT_HOME(caminho para o AndroidViewClient) no $HOME/.profile

   ex: export ANDROID_HOME=/Users/rlima/SDKs/android-sdk-macosx

       export ANDROID_VIEW_CLIENT_HOME=/Users/rlima/Documents/Code/AndroidViewClient/AndroidViewClient



Executando
==========

- Tenha um emulador com sdcard já rodando.
- Rodando os testes:

[CAMINHO_DO_MONKEYRUNNER] [TESTE.py]

ex: ~/SDKs/android-sdk-macosx/tools/monkeyrunner TestesCalculadora.py

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPTTpoNnvgjE4z2xwyW18FY",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/IsaqueR02/Python2/blob/main/Potencia.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O-n7miuIQi3x",
        "outputId": "a32b11ee-5bd7-4cee-a012-78b64e74ebb9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero: 15\n",
            "O dobro de 15 vale 30.\n",
            "O triplo de 15 vale 45. \n",
            "A raiz quadrada de 15 é igual a 3.872983346207417.\n"
          ]
        }
      ],
      "source": [
        "#Dobro, triplo e a raiz quadrada\n",
        "n = int(input('Digite um numero: '))\n",
        "d = n* 2\n",
        "t = n* 3\n",
        "r = n ** (1/2)\n",
        "print('O dobro de {} vale {}.'.format(n, d))\n",
        "print('O triplo de {} vale {}. \\nA raiz quadrada de {} é igual a {}.'.format(n, t, n, r))"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Dobro, triplo e a raiz quadrada(usando menos dados)\n",
        "n = int(input('Digite um numero: '))\n",
        "print('O dobro de {} vale {}.'.format(n, (n* 2)))\n",
        "print('O triplo de {} vale {}. \\nA raiz quadrada de {} é igual a {}.'.format(n, (n* 3), n, pow(n, (1/2))))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D6Cv-NVIUN1s",
        "outputId": "6d24e35d-fa68-4fd3-d1dd-a53e7df088aa"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um numero: 128\n",
            "O dobro de 128 vale 256.\n",
            "O triplo de 128 vale 384. \n",
            "A raiz quadrada de 128 é igual a 11.313708498984761.\n"
          ]
        }
      ]
    }
  ]
}
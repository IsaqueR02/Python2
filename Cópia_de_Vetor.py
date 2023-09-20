{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPzQfTCyLGX9cxKrbmC5xf2",
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
        "<a href=\"https://colab.research.google.com/github/IsaqueR02/Python2/blob/main/C%C3%B3pia_de_Vetor.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JcpmI4M_bi-T",
        "outputId": "c9a31934-bac2-4a56-ea82-26c93bd9b245"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "kkkkk10\n",
            "kkkkk11\n",
            "kkkkk11\n"
          ]
        }
      ],
      "source": [
        "isaque=[]\n",
        "for n in range(3):\n",
        "  isaque.append(int(input(\"kkkkk\")))\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#utilizando vetores\n",
        "num = []\n",
        "for n in range(3):\n",
        "  num.append(int(input('Digite: ')))\n",
        "\n",
        "for par in num:\n",
        "  if (par%2 == 0):\n",
        "    print(par)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ap7AoAHHrMz9",
        "outputId": "153915df-5f53-4bca-8698-84e36dcb60be"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite: 4\n",
            "Digite: 2\n",
            "Digite: 63\n",
            "4\n",
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#utilizando função\n",
        "def num(ber):\n",
        "  for n in ber:\n",
        "    if(n%2 == 0):\n",
        "      print(n)\n",
        "number=[]\n",
        "for n in range(3):\n",
        "  number.append(int(input('Digite: ')))\n",
        "\n",
        "num(number)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p1kxEnpm1he8",
        "outputId": "6a32b61d-4cb5-4def-d70c-5344be02135e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite: 1\n",
            "Digite: 3\n",
            "Digite: 2\n",
            "2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "vetor =[1,2,3]\n",
        "print(type(vetor))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RyupiqF-frZ8",
        "outputId": "7ab1b24c-9981-4a83-d67c-8de094031566"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'list'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "vetor =[1,2,3]\n",
        "vetor.append(5)\n",
        "#adicionando variaveis\n",
        "vetor.append(\"Vini\")\n",
        "vetor.append(input(\"Digite \"))\n",
        "print(vetor)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hmi40ldFgJ6_",
        "outputId": "88c01763-191e-474a-bd22-328ae8fa7139"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite 15\n",
            "[1, 2, 3, 5, 'Vini', '15']\n"
          ]
        }
      ]
    }
  ]
}

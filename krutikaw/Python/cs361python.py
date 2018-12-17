{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/krutikaw/CS361/blob/master/krutikaw/Python/cs361python.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "id": "UhLMt7uhDlEM",
        "colab_type": "code",
        "outputId": "e1a6c417-0f41-41b7-8e12-ac989100b2ce",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 353
        }
      },
      "cell_type": "code",
      "source": [
        "found = 0\n",
        "x = 11\n",
        "while found < 20:\n",
        "  if x%5 == 0 and x%7 == 0 and x%11 == 0:\n",
        "    print(x)\n",
        "    found = found+1\n",
        "  x = x+1\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "385\n",
            "770\n",
            "1155\n",
            "1540\n",
            "1925\n",
            "2310\n",
            "2695\n",
            "3080\n",
            "3465\n",
            "3850\n",
            "4235\n",
            "4620\n",
            "5005\n",
            "5390\n",
            "5775\n",
            "6160\n",
            "6545\n",
            "6930\n",
            "7315\n",
            "7700\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "33TNHam3j7t7",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "def isPrime(num):\n",
        "  if num > 1:\n",
        "\n",
        "    for i in range(2,num):\n",
        "      if (num % i) == 0:\n",
        "        \n",
        "        break\n",
        "      else:\n",
        "        print(\"True\")\n",
        "        break\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "kLr9PliokhNa",
        "colab_type": "code",
        "outputId": "f977bcea-11fe-4b57-952b-d14462cb5caa",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "isPrime(17)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "2vkMxthkkhbc",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "isPrime(16)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "59hBx0waESQk",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "def isPrime(num):\n",
        "  if num == 2 or num == 3:\n",
        "    print(\"True\")\n",
        "  elif (num % 6 == 1 or num % 6 == 5):\n",
        "    print(\"True\")\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "xOOfJ4K7EV-u",
        "colab_type": "code",
        "outputId": "9acc14eb-b6f0-40f3-ff8f-87b7401e1c4c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "isPrime(23)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "4GrZqHMaEj-k",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "def isPrime(num):\n",
        "  for i in range(num):\n",
        "    if i == 2 or i == 3:\n",
        "      print(i)\n",
        "    elif (i % 6 == 1 or i % 6 == 5):\n",
        "      print(i)\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "cdRfDh71Elsp",
        "colab_type": "code",
        "outputId": "6d5b8a80-f838-4450-bf28-f16a765fd8dd",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 134
        }
      },
      "cell_type": "code",
      "source": [
        "isPrime(17)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "5\n",
            "7\n",
            "11\n",
            "13\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "toLzbmPzlDlo",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "def isPrime(num):\n",
        "  i=0\n",
        "  while num>0:\n",
        "    if i == 2 or i == 3:\n",
        "      print(i)\n",
        "      num=num-1\n",
        "      i=i+1\n",
        "    elif (i % 6 == 1 or i % 6 == 5):\n",
        "      print(i)\n",
        "      num=num-1\n",
        "      i=i+1\n",
        "    else:\n",
        "      i=i+1\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "-it3qOB1oUVF",
        "colab_type": "code",
        "outputId": "0da10532-b9ed-4e7e-dbb8-2010a8c0cbbf",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 118
        }
      },
      "cell_type": "code",
      "source": [
        "isPrime(6)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "5\n",
            "7\n",
            "11\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "DhijX_Ge1z2u",
        "colab_type": "code",
        "outputId": "9cfa0907-112b-4816-ef3c-9f13f16cac5e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "def p(l):\n",
        "  for i in l:\n",
        "    print(i)\n",
        "p([2,3,4,5,6,7])"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[2, 3, 4, 5]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "JnQgEjrLAgjM",
        "colab_type": "code",
        "outputId": "89bf8994-e9fd-40cb-f8c8-073a7dd50a65",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        }
      },
      "cell_type": "code",
      "source": [
        "def pr():\n",
        "  for i in l[::-1]:\n",
        "    print(i)\n",
        "\n",
        "pr([2,3,4,5,6])"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "kjkv5CsRBFSr",
        "colab_type": "code",
        "outputId": "117d7564-bcaf-4485-c8e2-f82412f967e5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "def length(list):\n",
        "  j=0\n",
        "  for i in list:\n",
        "    j=j+1\n",
        "  return j\n",
        "\n",
        "length([2,3,4,5,6])\n",
        "  "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 206
        }
      ]
    },
    {
      "metadata": {
        "id": "F66Xx2eqEc7B",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "a =[1,2,3,4,5,6,7]\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "d7RPvqBMHAX7",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "b=a"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "YflkADQGHHBI",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "b[1]=4"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "oZGTYwcRHLyr",
        "colab_type": "code",
        "outputId": "1b37765b-8e7a-4bde-a8ad-b4c11fcef5fb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "print(a)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1, 4, 3, 4, 5, 6, 7]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "xB_5GYFkHP9B",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "c=a[:]"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "ZVmsh8kKIpv8",
        "colab_type": "code",
        "outputId": "27775cd1-9ce0-4cb3-8ed1-3c099cb756d1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "print(c)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1, 4, 10, 4, 5, 6, 7]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "-YIbUw36HUSi",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "c[2]=10"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "8bWru8UBHXwi",
        "colab_type": "code",
        "outputId": "0e112136-2e58-4610-c3c6-5c42f47b81b1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "print(a)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1, 4, 3, 4, 5, 6, 7]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "nMx2pF9yx5XY",
        "colab_type": "code",
        "outputId": "660140cc-f1f2-45d7-8583-bc037f6641df",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "def listnew(l):\n",
        "  finalList=[]\n",
        "  for list in l:\n",
        "    for ele in list:\n",
        "      finalList.append(ele)\n",
        "  print(finalList)\n",
        "\n",
        "listnew([[1,3],[3,6]])\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1, 3, 3, 6]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "67GvaKA4uryf",
        "colab_type": "code",
        "outputId": "2db7c3d1-099a-4ba9-b8e0-b60862a9187d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 393
        }
      },
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "x=np.linspace(0,2,100)\n",
        "\n",
        "y=np.sin(x-2)**(2)*2.718**(-(x**2))\n",
        "plt.xlabel(\"x-axis\")\n",
        "plt.ylabel(\"y-axis\")\n",
        "plt.title(\"Line Graph Example\")\n",
        "plt.plot(x,y)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f2f91bd5080>]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 198
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7f2f91bf91d0>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "metadata": {
        "id": "jXQODiZn22Ey",
        "colab_type": "code",
        "outputId": "767b7243-c64f-46d3-d693-4696dfb49bdb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "def product(ls):\n",
        "  if not ls:\n",
        "    return 1\n",
        " \n",
        "  return ls.pop()*product(ls)\n",
        "\n",
        "product([2,3,5,6])"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "180"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 34
        }
      ]
    },
    {
      "metadata": {
        "id": "Oaa8vSANFsk0",
        "colab_type": "code",
        "outputId": "3a80ed6d-c944-40d0-901c-a7b5b8a918cb",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "def product(ls):\n",
        "  prod=1;\n",
        "  for ele in ls:\n",
        "    prod=prod*ele\n",
        "  return prod\n",
        "product([2,3,5,6])\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "180"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 220
        }
      ]
    },
    {
      "metadata": {
        "id": "oNHaYETuGCzq",
        "colab_type": "code",
        "outputId": "3f82518d-57d3-4d54-e7ba-d6a4c1099dc1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "cell_type": "code",
      "source": [
        "def F(n):\n",
        "    if n == 0: \n",
        "      return 0\n",
        "    elif n == 1: \n",
        "      return 1\n",
        "    else: \n",
        "      return F(n-1)+F(n-2)\n",
        "\n",
        "F(6)\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "8"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 62
        }
      ]
    },
    {
      "metadata": {
        "id": "9YBmvantdLp9",
        "colab_type": "code",
        "outputId": "dd40493b-e4c2-4122-d6d6-81e078fdaa80",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 121
        }
      },
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Go to this URL in a browser: https://accounts.google.com/o/oauth2/auth?client_id=947318989803-6bn6qk8qdgf4n4g3pfee6491hc0brc4i.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=email%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdocs.test%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.photos.readonly%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fpeopleapi.readonly&response_type=code\n",
            "\n",
            "Enter your authorization code:\n",
            "··········\n",
            "Mounted at /content/drive\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "id": "9tnOrEq_bv0w",
        "colab_type": "code",
        "outputId": "1f15331f-bbfa-4069-8017-f742bdb753b5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 151
        }
      },
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "\n",
        "with open('input.txt', 'r') as f:\n",
        "  line = f.read()\n",
        "  match = re.findall(r'[\"?\\w\\.]+@[\\w\\.]+\\.\\w+', line)\n",
        "  for i in match:\n",
        "    print(i)\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "alice@stanford.com\n",
            "bob@spain.es\n",
            "email@addresses.com\n",
            "british@gmail.co.uk\n",
            "bob@gmail.com\n",
            "this@must.be\n",
            "\"very.unusual.@.unusual.com\n",
            "\"@example.com\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
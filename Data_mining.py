{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Abdulrahmansheier/Data_Mining/blob/main/Data_mining.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "36fb4be4",
      "metadata": {
        "id": "36fb4be4"
      },
      "source": [
        "# Importing libraries"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "0748894c",
      "metadata": {
        "id": "0748894c"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "import random\n",
        "from collections import defaultdict\n",
        "from pprint import pprint\n",
        "import nltk\n",
        "from nltk.corpus.reader import BNCCorpusReader\n",
        "from nltk.corpus.reader.plaintext import PlaintextCorpusReader\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, confusion_matrix\n",
        "import seaborn as sns\n",
        "from matplotlib import pyplot as plt\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "\n",
        "import tensorflow as tf\n",
        "from tensorflow import keras\n",
        "from tensorflow.keras import layers, losses, metrics\n",
        "\n",
        "from lxml import etree\n",
        "import altair as al"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8ab93404",
      "metadata": {
        "id": "8ab93404"
      },
      "outputs": [],
      "source": [
        "# Specifying the path directory\n",
        "path = r\"C:\\Users\\3mabd\\Desktop\\bnc2014spoken-xml\\spoken\"\n",
        "dir_corpus_tagged = os.path.join(path, \"tagged\")\n",
        "dir_corpus_untagged = os.path.join(path, \"untagged\")\n",
        "dir_meta = os.path.join(path, \"metadata\")"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "ea5b78d7",
      "metadata": {
        "id": "ea5b78d7"
      },
      "source": [
        "# Managing data from the utternce data"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "414585a9",
      "metadata": {
        "id": "414585a9"
      },
      "outputs": [],
      "source": [
        "# First ill be printing the utterence data to view it from the untagged corpus"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c3c523f9",
      "metadata": {
        "scrolled": true,
        "id": "c3c523f9",
        "outputId": "9b59b8a9-cfae-44e0-b7dc-8ba41a4129bd"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>n</th>\n",
              "      <th>who</th>\n",
              "      <th>u</th>\n",
              "      <th>unclear</th>\n",
              "      <th>trans</th>\n",
              "      <th>whoConfidence</th>\n",
              "      <th>vocal</th>\n",
              "      <th>foreign</th>\n",
              "      <th>anon</th>\n",
              "      <th>pause</th>\n",
              "      <th>trunc</th>\n",
              "      <th>shift</th>\n",
              "      <th>event</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>S0094</td>\n",
              "      <td>words</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>S0095</td>\n",
              "      <td>it's a games word? like a computer games word?</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>S0032</td>\n",
              "      <td>yeah yeah</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>S0095</td>\n",
              "      <td>oh</td>\n",
              "      <td>oh that's nice</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>S0032</td>\n",
              "      <td>I it's something I</td>\n",
              "      <td>have really heard</td>\n",
              "      <td>overlap</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1248105</th>\n",
              "      <td>316</td>\n",
              "      <td>S0432</td>\n",
              "      <td>but</td>\n",
              "      <td>Mai Li</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1248106</th>\n",
              "      <td>317</td>\n",
              "      <td>S0428</td>\n",
              "      <td>None</td>\n",
              "      <td>Sha Li</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1248107</th>\n",
              "      <td>318</td>\n",
              "      <td>S0432</td>\n",
              "      <td>I'll just stick with it yeah</td>\n",
              "      <td>None</td>\n",
              "      <td>overlap</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>let</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1248108</th>\n",
              "      <td>319</td>\n",
              "      <td>S0428</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>overlap</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1248109</th>\n",
              "      <td>320</td>\n",
              "      <td>S0432</td>\n",
              "      <td>mm</td>\n",
              "      <td>None</td>\n",
              "      <td>overlap</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1248110 rows × 13 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "           n    who                                               u  \\\n",
              "0          1  S0094                                           words   \n",
              "1          2  S0095  it's a games word? like a computer games word?   \n",
              "2          3  S0032                                       yeah yeah   \n",
              "3          4  S0095                                              oh   \n",
              "4          5  S0032                              I it's something I   \n",
              "...      ...    ...                                             ...   \n",
              "1248105  316  S0432                                             but   \n",
              "1248106  317  S0428                                            None   \n",
              "1248107  318  S0432                    I'll just stick with it yeah   \n",
              "1248108  319  S0428                                            None   \n",
              "1248109  320  S0432                                              mm   \n",
              "\n",
              "                   unclear    trans whoConfidence  vocal foreign  anon  pause  \\\n",
              "0                     None     None          None    NaN    None   NaN    NaN   \n",
              "1                     None     None          None    NaN    None   NaN    NaN   \n",
              "2                     None     None          None    NaN    None   NaN    NaN   \n",
              "3           oh that's nice     None          None    NaN    None   NaN    NaN   \n",
              "4        have really heard  overlap          None    NaN    None   NaN    NaN   \n",
              "...                    ...      ...           ...    ...     ...   ...    ...   \n",
              "1248105             Mai Li     None          None    NaN     NaN   NaN    NaN   \n",
              "1248106             Sha Li     None          None    NaN     NaN   NaN    NaN   \n",
              "1248107               None  overlap          None    NaN     NaN   NaN    NaN   \n",
              "1248108               None  overlap          None    NaN     NaN   NaN    NaN   \n",
              "1248109               None  overlap          None    NaN     NaN   NaN    NaN   \n",
              "\n",
              "        trunc  shift  event  \n",
              "0        None    NaN    NaN  \n",
              "1        None    NaN    NaN  \n",
              "2        None    NaN    NaN  \n",
              "3        None    NaN    NaN  \n",
              "4        None    NaN    NaN  \n",
              "...       ...    ...    ...  \n",
              "1248105  None    NaN    NaN  \n",
              "1248106  None    NaN    NaN  \n",
              "1248107   let    NaN    NaN  \n",
              "1248108  None    NaN    NaN  \n",
              "1248109  None    NaN    NaN  \n",
              "\n",
              "[1248110 rows x 13 columns]"
            ]
          },
          "execution_count": 4,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "def read(dir, xpath):\n",
        "    f_names = os.listdir(dir)\n",
        "    f_paths = [f\"{dir}/{name}\" for name in f_names]\n",
        "    units = []\n",
        "\n",
        "    for path in f_paths:\n",
        "        block = pd.read_xml(path, xpath=xpath, encoding='utf-8')\n",
        "        units.append(block)\n",
        "\n",
        "    frame = pd.concat(units, axis=0, ignore_index=True)\n",
        "    return frame\n",
        "\n",
        "df = read(dir_corpus_untagged, '//u')\n",
        "df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "b512d4b9",
      "metadata": {
        "id": "b512d4b9"
      },
      "outputs": [],
      "source": [
        "# This code is for changing the type to string\n",
        "df['u'] = df['u'].astype('string')\n",
        "# This part is for remving any Null values\n",
        "df =  df[df['u'] != '<NA>']"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "836a2f55",
      "metadata": {
        "id": "836a2f55",
        "outputId": "291862e5-02a8-444c-a6dc-b7f115eb9f30"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "n                      0\n",
              "who                    0\n",
              "u                      0\n",
              "unclear          1103183\n",
              "trans             891784\n",
              "whoConfidence    1096240\n",
              "vocal            1119744\n",
              "foreign          1119262\n",
              "anon             1119744\n",
              "pause            1119744\n",
              "trunc            1068040\n",
              "shift            1119744\n",
              "event            1119744\n",
              "dtype: int64"
            ]
          },
          "execution_count": 6,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# getting the number of missing data points per column\n",
        "missing_values_count = df.isnull().sum()\n",
        "# missing points in the columns\n",
        "missing_values_count"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "312b5fed",
      "metadata": {
        "id": "312b5fed"
      },
      "outputs": [],
      "source": [
        "# remove all the rows that contain a missing value\n",
        "df = df.dropna(axis=1)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "ca70b892",
      "metadata": {
        "id": "ca70b892",
        "outputId": "db1c2ea6-4715-4a09-8a6c-be8784a9e973"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "n      0\n",
              "who    0\n",
              "u      0\n",
              "dtype: int64"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# get the number of missing data points per column in the utterance\n",
        "missing_values_count = df.isnull().sum()\n",
        "# missing points in the columns\n",
        "missing_values_count"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1df855ea",
      "metadata": {
        "id": "1df855ea",
        "outputId": "25ffaa68-0dd0-468e-b821-4d3a364c22d3"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>n</th>\n",
              "      <th>who</th>\n",
              "      <th>u</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>S0094</td>\n",
              "      <td>words</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>S0095</td>\n",
              "      <td>it's a games word? like a computer games word?</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>S0032</td>\n",
              "      <td>yeah yeah</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>S0095</td>\n",
              "      <td>oh</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>S0032</td>\n",
              "      <td>I it's something I</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1248099</th>\n",
              "      <td>310</td>\n",
              "      <td>S0432</td>\n",
              "      <td>yeah</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1248100</th>\n",
              "      <td>311</td>\n",
              "      <td>S0428</td>\n",
              "      <td>Little Jasmine</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1248105</th>\n",
              "      <td>316</td>\n",
              "      <td>S0432</td>\n",
              "      <td>but</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1248107</th>\n",
              "      <td>318</td>\n",
              "      <td>S0432</td>\n",
              "      <td>I'll just stick with it yeah</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1248109</th>\n",
              "      <td>320</td>\n",
              "      <td>S0432</td>\n",
              "      <td>mm</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1119744 rows × 3 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "           n    who                                               u\n",
              "0          1  S0094                                           words\n",
              "1          2  S0095  it's a games word? like a computer games word?\n",
              "2          3  S0032                                       yeah yeah\n",
              "3          4  S0095                                              oh\n",
              "4          5  S0032                              I it's something I\n",
              "...      ...    ...                                             ...\n",
              "1248099  310  S0432                                            yeah\n",
              "1248100  311  S0428                                  Little Jasmine\n",
              "1248105  316  S0432                                             but\n",
              "1248107  318  S0432                    I'll just stick with it yeah\n",
              "1248109  320  S0432                                              mm\n",
              "\n",
              "[1119744 rows x 3 columns]"
            ]
          },
          "execution_count": 9,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# Inspecting the U file after removing the columns with the missing values\n",
        "df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f0ba9af6",
      "metadata": {
        "id": "f0ba9af6",
        "outputId": "8f3ac57e-4f64-49b3-f2a1-9d81af44c46a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "who\n",
            "S0001        27.627119\n",
            "S0002        26.239700\n",
            "S0003        27.650602\n",
            "S0004        32.746130\n",
            "S0005        30.714286\n",
            "               ...    \n",
            "S0691        27.050000\n",
            "S0692        21.859756\n",
            "UNKFEMALE    17.482796\n",
            "UNKMALE      19.669201\n",
            "UNKMULTI      6.035928\n",
            "Name: u, Length: 671, dtype: float64\n"
          ]
        }
      ],
      "source": [
        "# group data by speaker and calculate mean utterance length per speaker\n",
        "mean_utterance_length = df.groupby('who')['u'].apply(lambda x: x.str.len().mean())\n",
        "print(mean_utterance_length)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "06a558ba",
      "metadata": {
        "id": "06a558ba",
        "outputId": "3215ee5d-b25a-4410-b213-8d09e2f63caa"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "       count        mean          std  min    25%    50%     75%      max  \\\n",
            "n  1119744.0  947.209766  1324.344264  1.0  252.0  586.0  1205.0  16574.0   \n",
            "\n",
            "     range  \n",
            "n  16573.0  \n"
          ]
        }
      ],
      "source": [
        "# choosing the three columns in the utterence table\n",
        "df_utterence = df[['n', 'who', 'u']]\n",
        "\n",
        "# create summary statistics table\n",
        "summary_statistics = df_utterence.describe(percentiles=[0.25, 0.5, 0.75]).transpose()\n",
        "# adding the range column to summary table\n",
        "summary_statistics['range'] = summary_statistics['max'] - summary_statistics['min']\n",
        "# reorder columns\n",
        "summary_statistics = summary_statistics[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'range']]\n",
        "\n",
        "# print summary table\n",
        "print(summary_statistics)\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "653cd6eb",
      "metadata": {
        "id": "653cd6eb"
      },
      "source": [
        "# Managing data from the speakers data"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "329312e0",
      "metadata": {
        "id": "329312e0"
      },
      "outputs": [],
      "source": [
        "# printing the speakers data to view it"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1e526f32",
      "metadata": {
        "id": "1e526f32",
        "outputId": "5bdffe3f-a205-4253-a26d-34b13e8e0d12"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>exactage</th>\n",
              "      <th>age1994</th>\n",
              "      <th>agerange</th>\n",
              "      <th>gender</th>\n",
              "      <th>nat</th>\n",
              "      <th>birthplace</th>\n",
              "      <th>birthcountry</th>\n",
              "      <th>l1</th>\n",
              "      <th>lingorig</th>\n",
              "      <th>...</th>\n",
              "      <th>dialect_l2</th>\n",
              "      <th>dialect_l3</th>\n",
              "      <th>dialect_l4</th>\n",
              "      <th>edqual</th>\n",
              "      <th>occupation</th>\n",
              "      <th>socgrade</th>\n",
              "      <th>nssec</th>\n",
              "      <th>l2</th>\n",
              "      <th>fls</th>\n",
              "      <th>in_core</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>S0021</td>\n",
              "      <td>27</td>\n",
              "      <td>25_34</td>\n",
              "      <td>19_29</td>\n",
              "      <td>F</td>\n",
              "      <td>British</td>\n",
              "      <td>Swindon</td>\n",
              "      <td>England</td>\n",
              "      <td>English</td>\n",
              "      <td>England</td>\n",
              "      <td>...</td>\n",
              "      <td>england</td>\n",
              "      <td>south</td>\n",
              "      <td>southwest</td>\n",
              "      <td>5_postgrad</td>\n",
              "      <td>Teacher</td>\n",
              "      <td>B</td>\n",
              "      <td>2</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>S0032</td>\n",
              "      <td>28</td>\n",
              "      <td>25_34</td>\n",
              "      <td>19_29</td>\n",
              "      <td>M</td>\n",
              "      <td>British</td>\n",
              "      <td>Yoevil</td>\n",
              "      <td>England</td>\n",
              "      <td>English</td>\n",
              "      <td>England</td>\n",
              "      <td>...</td>\n",
              "      <td>england</td>\n",
              "      <td>south</td>\n",
              "      <td>southwest</td>\n",
              "      <td>4_graduate</td>\n",
              "      <td>Software developer</td>\n",
              "      <td>A</td>\n",
              "      <td>1_2</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>S0094</td>\n",
              "      <td>33</td>\n",
              "      <td>25_34</td>\n",
              "      <td>30_39</td>\n",
              "      <td>F</td>\n",
              "      <td>British</td>\n",
              "      <td>Swindon</td>\n",
              "      <td>England</td>\n",
              "      <td>English</td>\n",
              "      <td>England</td>\n",
              "      <td>...</td>\n",
              "      <td>england</td>\n",
              "      <td>south</td>\n",
              "      <td>southwest</td>\n",
              "      <td>5_postgrad</td>\n",
              "      <td>PhD student</td>\n",
              "      <td>A</td>\n",
              "      <td>1_2</td>\n",
              "      <td>German</td>\n",
              "      <td>Welsh -- Beginner</td>\n",
              "      <td>y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>S0095</td>\n",
              "      <td>33</td>\n",
              "      <td>25_34</td>\n",
              "      <td>30_39</td>\n",
              "      <td>M</td>\n",
              "      <td>British</td>\n",
              "      <td>Camarthen</td>\n",
              "      <td>Scotland</td>\n",
              "      <td>English</td>\n",
              "      <td>England</td>\n",
              "      <td>...</td>\n",
              "      <td>wales</td>\n",
              "      <td>wales</td>\n",
              "      <td>wales</td>\n",
              "      <td>5_postgrad</td>\n",
              "      <td>Self employed maker</td>\n",
              "      <td>E</td>\n",
              "      <td>uncat</td>\n",
              "      <td>None</td>\n",
              "      <td>None</td>\n",
              "      <td>y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>S0261</td>\n",
              "      <td>41</td>\n",
              "      <td>35_44</td>\n",
              "      <td>40_49</td>\n",
              "      <td>M</td>\n",
              "      <td>British/New Zealand</td>\n",
              "      <td>Wellington</td>\n",
              "      <td>New Zealand</td>\n",
              "      <td>English</td>\n",
              "      <td>England/NZ</td>\n",
              "      <td>...</td>\n",
              "      <td>non_uk</td>\n",
              "      <td>non_uk</td>\n",
              "      <td>non_uk</td>\n",
              "      <td>4_graduate</td>\n",
              "      <td>Entrepreneur</td>\n",
              "      <td>A</td>\n",
              "      <td>1_2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>n</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3588</th>\n",
              "      <td>S0510</td>\n",
              "      <td>47</td>\n",
              "      <td>45_59</td>\n",
              "      <td>40_49</td>\n",
              "      <td>F</td>\n",
              "      <td>British</td>\n",
              "      <td>England</td>\n",
              "      <td>England</td>\n",
              "      <td>English</td>\n",
              "      <td>England</td>\n",
              "      <td>...</td>\n",
              "      <td>england</td>\n",
              "      <td>south</td>\n",
              "      <td>unspecified</td>\n",
              "      <td>5_postgrad</td>\n",
              "      <td>Receptionist</td>\n",
              "      <td>D</td>\n",
              "      <td>6</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3589</th>\n",
              "      <td>S0058</td>\n",
              "      <td>23</td>\n",
              "      <td>15_24</td>\n",
              "      <td>19_29</td>\n",
              "      <td>F</td>\n",
              "      <td>British</td>\n",
              "      <td>Sunderland, Tyne and Wear</td>\n",
              "      <td>England</td>\n",
              "      <td>English</td>\n",
              "      <td>England</td>\n",
              "      <td>...</td>\n",
              "      <td>england</td>\n",
              "      <td>north</td>\n",
              "      <td>northeast</td>\n",
              "      <td>4_graduate</td>\n",
              "      <td>Corpus Administrator</td>\n",
              "      <td>B</td>\n",
              "      <td>2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>None</td>\n",
              "      <td>n</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3590</th>\n",
              "      <td>S0120</td>\n",
              "      <td>23</td>\n",
              "      <td>15_24</td>\n",
              "      <td>19_29</td>\n",
              "      <td>M</td>\n",
              "      <td>British &amp; German</td>\n",
              "      <td>Pembury, Kent</td>\n",
              "      <td>England</td>\n",
              "      <td>English</td>\n",
              "      <td>England</td>\n",
              "      <td>...</td>\n",
              "      <td>england</td>\n",
              "      <td>south</td>\n",
              "      <td>unspecified</td>\n",
              "      <td>5_postgrad</td>\n",
              "      <td>Graduate Civil Engineer</td>\n",
              "      <td>C1</td>\n",
              "      <td>4</td>\n",
              "      <td>NaN</td>\n",
              "      <td>German -- Advanced; French -- Advanced</td>\n",
              "      <td>n</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3591</th>\n",
              "      <td>S0428</td>\n",
              "      <td>27</td>\n",
              "      <td>25_34</td>\n",
              "      <td>19_29</td>\n",
              "      <td>F</td>\n",
              "      <td>British</td>\n",
              "      <td>Aylesbury, Buckinghamshire</td>\n",
              "      <td>England</td>\n",
              "      <td>English</td>\n",
              "      <td>England</td>\n",
              "      <td>...</td>\n",
              "      <td>england</td>\n",
              "      <td>south</td>\n",
              "      <td>eastern_engl</td>\n",
              "      <td>5_postgrad</td>\n",
              "      <td>Language Research Co-ordinator</td>\n",
              "      <td>A</td>\n",
              "      <td>1_2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Spanish -- level unspecified; Italian -- level...</td>\n",
              "      <td>y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3592</th>\n",
              "      <td>S0432</td>\n",
              "      <td>23</td>\n",
              "      <td>15_24</td>\n",
              "      <td>19_29</td>\n",
              "      <td>F</td>\n",
              "      <td>White British</td>\n",
              "      <td>Lincoln</td>\n",
              "      <td>England</td>\n",
              "      <td>English</td>\n",
              "      <td>England</td>\n",
              "      <td>...</td>\n",
              "      <td>england</td>\n",
              "      <td>unspecified</td>\n",
              "      <td>unspecified</td>\n",
              "      <td>4_graduate</td>\n",
              "      <td>Language Research Administrator</td>\n",
              "      <td>A</td>\n",
              "      <td>1_2</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Spanish -- level unspecified; Chinese -- level...</td>\n",
              "      <td>n</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>3593 rows × 25 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "         id exactage age1994 agerange gender                  nat  \\\n",
              "0     S0021       27   25_34    19_29      F              British   \n",
              "1     S0032       28   25_34    19_29      M              British   \n",
              "2     S0094       33   25_34    30_39      F              British   \n",
              "3     S0095       33   25_34    30_39      M              British   \n",
              "4     S0261       41   35_44    40_49      M  British/New Zealand   \n",
              "...     ...      ...     ...      ...    ...                  ...   \n",
              "3588  S0510       47   45_59    40_49      F              British   \n",
              "3589  S0058       23   15_24    19_29      F              British   \n",
              "3590  S0120       23   15_24    19_29      M     British & German   \n",
              "3591  S0428       27   25_34    19_29      F              British   \n",
              "3592  S0432       23   15_24    19_29      F        White British   \n",
              "\n",
              "                      birthplace birthcountry       l1    lingorig  ...  \\\n",
              "0                        Swindon      England  English     England  ...   \n",
              "1                         Yoevil      England  English     England  ...   \n",
              "2                        Swindon      England  English     England  ...   \n",
              "3                      Camarthen     Scotland  English     England  ...   \n",
              "4                     Wellington  New Zealand  English  England/NZ  ...   \n",
              "...                          ...          ...      ...         ...  ...   \n",
              "3588                     England      England  English     England  ...   \n",
              "3589   Sunderland, Tyne and Wear      England  English     England  ...   \n",
              "3590               Pembury, Kent      England  English     England  ...   \n",
              "3591  Aylesbury, Buckinghamshire      England  English     England  ...   \n",
              "3592                     Lincoln      England  English     England  ...   \n",
              "\n",
              "     dialect_l2   dialect_l3    dialect_l4      edqual  \\\n",
              "0       england        south     southwest  5_postgrad   \n",
              "1       england        south     southwest  4_graduate   \n",
              "2       england        south     southwest  5_postgrad   \n",
              "3         wales        wales         wales  5_postgrad   \n",
              "4        non_uk       non_uk        non_uk  4_graduate   \n",
              "...         ...          ...           ...         ...   \n",
              "3588    england        south   unspecified  5_postgrad   \n",
              "3589    england        north     northeast  4_graduate   \n",
              "3590    england        south   unspecified  5_postgrad   \n",
              "3591    england        south  eastern_engl  5_postgrad   \n",
              "3592    england  unspecified   unspecified  4_graduate   \n",
              "\n",
              "                           occupation socgrade  nssec      l2  \\\n",
              "0                             Teacher        B      2    None   \n",
              "1                  Software developer        A    1_2    None   \n",
              "2                         PhD student        A    1_2  German   \n",
              "3                 Self employed maker        E  uncat    None   \n",
              "4                        Entrepreneur        A    1_2     NaN   \n",
              "...                               ...      ...    ...     ...   \n",
              "3588                     Receptionist        D      6     NaN   \n",
              "3589             Corpus Administrator        B      2     NaN   \n",
              "3590          Graduate Civil Engineer       C1      4     NaN   \n",
              "3591   Language Research Co-ordinator        A    1_2     NaN   \n",
              "3592  Language Research Administrator        A    1_2     NaN   \n",
              "\n",
              "                                                    fls in_core  \n",
              "0                                                  None       y  \n",
              "1                                                  None       y  \n",
              "2                                     Welsh -- Beginner       y  \n",
              "3                                                  None       y  \n",
              "4                                                  None       n  \n",
              "...                                                 ...     ...  \n",
              "3588                                                NaN       y  \n",
              "3589                                               None       n  \n",
              "3590             German -- Advanced; French -- Advanced       n  \n",
              "3591  Spanish -- level unspecified; Italian -- level...       y  \n",
              "3592  Spanish -- level unspecified; Chinese -- level...       n  \n",
              "\n",
              "[3593 rows x 25 columns]"
            ]
          },
          "execution_count": 13,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "def read(dir, xpath):\n",
        "    f_names = os.listdir(dir)\n",
        "    f_paths = [f\"{dir}/{name}\" for name in f_names]\n",
        "    units = []\n",
        "\n",
        "    for path in f_paths:\n",
        "        block = pd.read_xml(path, xpath=xpath, encoding='utf-8')\n",
        "        units.append(block)\n",
        "\n",
        "    frame = pd.concat(units, axis=0, ignore_index=True)\n",
        "    return frame\n",
        "\n",
        "df_speaker = read(dir_corpus_untagged, '//speaker')\n",
        "df_speaker"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d1159302",
      "metadata": {
        "scrolled": true,
        "id": "d1159302",
        "outputId": "9d5980df-7072-4772-b5e8-1d4c0418051e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "           count       mean        std  min   25%   50%   75%   max  range\n",
            "exactage  3233.0  37.603155  19.605057  2.0  21.0  36.0  53.0  91.0   89.0\n"
          ]
        }
      ],
      "source": [
        "# select age-related columns / columns of interest\n",
        "age_columns = ['exactage']\n",
        "#exactage' converting it to a numeric type using the pd.to_numeric function\n",
        "df_speaker[age_columns] = df_speaker[age_columns].apply(pd.to_numeric, errors='coerce')\n",
        "# create summary statistics table\n",
        "summary_statistics = df_speaker[age_columns].describe(percentiles=[0.25, 0.5, 0.75]).transpose()\n",
        "# add range column to summary table\n",
        "summary_statistics['range'] = summary_statistics['max'] - summary_statistics['min']\n",
        "# reorder columns\n",
        "summary_statistics = summary_statistics[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max', 'range']]\n",
        "# print summary table\n",
        "print(summary_statistics)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "c817d326",
      "metadata": {
        "id": "c817d326",
        "outputId": "993b8689-c9d6-4841-e9b6-2e3b1533fbe4"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>age1994</th>\n",
              "      <th>agerange</th>\n",
              "      <th>gender</th>\n",
              "      <th>dialect_rep</th>\n",
              "      <th>dialect_l1</th>\n",
              "      <th>dialect_l2</th>\n",
              "      <th>dialect_l3</th>\n",
              "      <th>dialect_l4</th>\n",
              "      <th>edqual</th>\n",
              "      <th>socgrade</th>\n",
              "      <th>nssec</th>\n",
              "      <th>in_core</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>S0021</td>\n",
              "      <td>25_34</td>\n",
              "      <td>19_29</td>\n",
              "      <td>F</td>\n",
              "      <td>West Country</td>\n",
              "      <td>uk</td>\n",
              "      <td>england</td>\n",
              "      <td>south</td>\n",
              "      <td>southwest</td>\n",
              "      <td>5_postgrad</td>\n",
              "      <td>B</td>\n",
              "      <td>2</td>\n",
              "      <td>y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>S0032</td>\n",
              "      <td>25_34</td>\n",
              "      <td>19_29</td>\n",
              "      <td>M</td>\n",
              "      <td>South West</td>\n",
              "      <td>uk</td>\n",
              "      <td>england</td>\n",
              "      <td>south</td>\n",
              "      <td>southwest</td>\n",
              "      <td>4_graduate</td>\n",
              "      <td>A</td>\n",
              "      <td>1_2</td>\n",
              "      <td>y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>S0094</td>\n",
              "      <td>25_34</td>\n",
              "      <td>30_39</td>\n",
              "      <td>F</td>\n",
              "      <td>West Country</td>\n",
              "      <td>uk</td>\n",
              "      <td>england</td>\n",
              "      <td>south</td>\n",
              "      <td>southwest</td>\n",
              "      <td>5_postgrad</td>\n",
              "      <td>A</td>\n",
              "      <td>1_2</td>\n",
              "      <td>y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>S0095</td>\n",
              "      <td>25_34</td>\n",
              "      <td>30_39</td>\n",
              "      <td>M</td>\n",
              "      <td>Slightly Welsh</td>\n",
              "      <td>uk</td>\n",
              "      <td>wales</td>\n",
              "      <td>wales</td>\n",
              "      <td>wales</td>\n",
              "      <td>5_postgrad</td>\n",
              "      <td>E</td>\n",
              "      <td>uncat</td>\n",
              "      <td>y</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>S0261</td>\n",
              "      <td>35_44</td>\n",
              "      <td>40_49</td>\n",
              "      <td>M</td>\n",
              "      <td>Kiwi English</td>\n",
              "      <td>non_uk</td>\n",
              "      <td>non_uk</td>\n",
              "      <td>non_uk</td>\n",
              "      <td>non_uk</td>\n",
              "      <td>4_graduate</td>\n",
              "      <td>A</td>\n",
              "      <td>1_2</td>\n",
              "      <td>n</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      id age1994 agerange gender     dialect_rep dialect_l1 dialect_l2  \\\n",
              "0  S0021   25_34    19_29      F    West Country         uk    england   \n",
              "1  S0032   25_34    19_29      M      South West         uk    england   \n",
              "2  S0094   25_34    30_39      F    West Country         uk    england   \n",
              "3  S0095   25_34    30_39      M  Slightly Welsh         uk      wales   \n",
              "4  S0261   35_44    40_49      M    Kiwi English     non_uk     non_uk   \n",
              "\n",
              "  dialect_l3 dialect_l4      edqual socgrade  nssec in_core  \n",
              "0      south  southwest  5_postgrad        B      2       y  \n",
              "1      south  southwest  4_graduate        A    1_2       y  \n",
              "2      south  southwest  5_postgrad        A    1_2       y  \n",
              "3      wales      wales  5_postgrad        E  uncat       y  \n",
              "4     non_uk     non_uk  4_graduate        A    1_2       n  "
            ]
          },
          "execution_count": 15,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# remove all columns with at least one missing value\n",
        "columns_with_na_dropped = df_speaker.dropna(axis=1)\n",
        "columns_with_na_dropped.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "e67cbb8b",
      "metadata": {
        "id": "e67cbb8b"
      },
      "source": [
        "#  Extracting the columns from df_speaker and merging it to Utternce"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "2687bbd4",
      "metadata": {
        "id": "2687bbd4"
      },
      "outputs": [],
      "source": [
        "age_columns = ['exactage', 'age1994', 'agerange']\n",
        "df_age = df_speaker[age_columns]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "4ab4cf6b",
      "metadata": {
        "id": "4ab4cf6b",
        "outputId": "ea3937cb-6bb9-49bf-caf8-5178cdfbb735"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>n</th>\n",
              "      <th>who</th>\n",
              "      <th>u</th>\n",
              "      <th>exactage</th>\n",
              "      <th>age1994</th>\n",
              "      <th>agerange</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1.0</td>\n",
              "      <td>S0094</td>\n",
              "      <td>words</td>\n",
              "      <td>27</td>\n",
              "      <td>25_34</td>\n",
              "      <td>19_29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2.0</td>\n",
              "      <td>S0095</td>\n",
              "      <td>it's a games word? like a computer games word?</td>\n",
              "      <td>28</td>\n",
              "      <td>25_34</td>\n",
              "      <td>19_29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3.0</td>\n",
              "      <td>S0032</td>\n",
              "      <td>yeah yeah</td>\n",
              "      <td>33</td>\n",
              "      <td>25_34</td>\n",
              "      <td>30_39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4.0</td>\n",
              "      <td>S0095</td>\n",
              "      <td>oh</td>\n",
              "      <td>33</td>\n",
              "      <td>25_34</td>\n",
              "      <td>30_39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5.0</td>\n",
              "      <td>S0032</td>\n",
              "      <td>I it's something I</td>\n",
              "      <td>41</td>\n",
              "      <td>35_44</td>\n",
              "      <td>40_49</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3557</th>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>59</td>\n",
              "      <td>45_59</td>\n",
              "      <td>50_59</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3558</th>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>32</td>\n",
              "      <td>25_34</td>\n",
              "      <td>30_39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3567</th>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>59</td>\n",
              "      <td>45_59</td>\n",
              "      <td>50_59</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3569</th>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>23</td>\n",
              "      <td>15_24</td>\n",
              "      <td>19_29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3573</th>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>&lt;NA&gt;</td>\n",
              "      <td>23</td>\n",
              "      <td>15_24</td>\n",
              "      <td>19_29</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1120538 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "        n    who                                               u exactage  \\\n",
              "0     1.0  S0094                                           words       27   \n",
              "1     2.0  S0095  it's a games word? like a computer games word?       28   \n",
              "2     3.0  S0032                                       yeah yeah       33   \n",
              "3     4.0  S0095                                              oh       33   \n",
              "4     5.0  S0032                              I it's something I       41   \n",
              "...   ...    ...                                             ...      ...   \n",
              "3557  NaN    NaN                                            <NA>       59   \n",
              "3558  NaN    NaN                                            <NA>       32   \n",
              "3567  NaN    NaN                                            <NA>       59   \n",
              "3569  NaN    NaN                                            <NA>       23   \n",
              "3573  NaN    NaN                                            <NA>       23   \n",
              "\n",
              "     age1994 agerange  \n",
              "0      25_34    19_29  \n",
              "1      25_34    19_29  \n",
              "2      25_34    30_39  \n",
              "3      25_34    30_39  \n",
              "4      35_44    40_49  \n",
              "...      ...      ...  \n",
              "3557   45_59    50_59  \n",
              "3558   25_34    30_39  \n",
              "3567   45_59    50_59  \n",
              "3569   15_24    19_29  \n",
              "3573   15_24    19_29  \n",
              "\n",
              "[1120538 rows x 6 columns]"
            ]
          },
          "execution_count": 17,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# getting the speaker data\n",
        "df_speaker = read(dir_corpus_untagged, '//speaker')\n",
        "# selecting age-related columns\n",
        "age_columns = ['exactage', 'age1994', 'agerange']\n",
        "\n",
        "# merge age-related columns to df\n",
        "df_new = pd.concat([df, df_speaker[age_columns]], axis=1)\n",
        "df_new"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "cb6be740",
      "metadata": {
        "id": "cb6be740"
      },
      "source": [
        "# Cleaning the new dataframe created"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "52c8d088",
      "metadata": {
        "id": "52c8d088"
      },
      "outputs": [],
      "source": [
        "df_new = pd.concat([df, df_speaker[age_columns]], axis=1)\n",
        "df_new = df_new.dropna(subset=['who', 'exactage','age1994','agerange'])\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "d734c691",
      "metadata": {
        "id": "d734c691",
        "outputId": "4baf9b53-6f94-4547-89a5-4c2c6f678d1e"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>n</th>\n",
              "      <th>who</th>\n",
              "      <th>u</th>\n",
              "      <th>exactage</th>\n",
              "      <th>age1994</th>\n",
              "      <th>agerange</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1.0</td>\n",
              "      <td>S0094</td>\n",
              "      <td>words</td>\n",
              "      <td>27</td>\n",
              "      <td>25_34</td>\n",
              "      <td>19_29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2.0</td>\n",
              "      <td>S0095</td>\n",
              "      <td>it's a games word? like a computer games word?</td>\n",
              "      <td>28</td>\n",
              "      <td>25_34</td>\n",
              "      <td>19_29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3.0</td>\n",
              "      <td>S0032</td>\n",
              "      <td>yeah yeah</td>\n",
              "      <td>33</td>\n",
              "      <td>25_34</td>\n",
              "      <td>30_39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4.0</td>\n",
              "      <td>S0095</td>\n",
              "      <td>oh</td>\n",
              "      <td>33</td>\n",
              "      <td>25_34</td>\n",
              "      <td>30_39</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5.0</td>\n",
              "      <td>S0032</td>\n",
              "      <td>I it's something I</td>\n",
              "      <td>41</td>\n",
              "      <td>35_44</td>\n",
              "      <td>40_49</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3588</th>\n",
              "      <td>3589.0</td>\n",
              "      <td>S0032</td>\n",
              "      <td>blow to bits</td>\n",
              "      <td>47</td>\n",
              "      <td>45_59</td>\n",
              "      <td>40_49</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3589</th>\n",
              "      <td>3590.0</td>\n",
              "      <td>S0094</td>\n",
              "      <td>yeah that's the only one that like makes sense</td>\n",
              "      <td>23</td>\n",
              "      <td>15_24</td>\n",
              "      <td>19_29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3590</th>\n",
              "      <td>3591.0</td>\n",
              "      <td>S0021</td>\n",
              "      <td>well I use gib in a very different like meanin...</td>\n",
              "      <td>23</td>\n",
              "      <td>15_24</td>\n",
              "      <td>19_29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3591</th>\n",
              "      <td>3592.0</td>\n",
              "      <td>S0032</td>\n",
              "      <td>what meaning do you use?</td>\n",
              "      <td>27</td>\n",
              "      <td>25_34</td>\n",
              "      <td>19_29</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3592</th>\n",
              "      <td>3593.0</td>\n",
              "      <td>S0021</td>\n",
              "      <td>well we sort of just say gib</td>\n",
              "      <td>23</td>\n",
              "      <td>15_24</td>\n",
              "      <td>19_29</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>2525 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "           n    who                                                  u  \\\n",
              "0        1.0  S0094                                              words   \n",
              "1        2.0  S0095     it's a games word? like a computer games word?   \n",
              "2        3.0  S0032                                          yeah yeah   \n",
              "3        4.0  S0095                                                 oh   \n",
              "4        5.0  S0032                                 I it's something I   \n",
              "...      ...    ...                                                ...   \n",
              "3588  3589.0  S0032                                       blow to bits   \n",
              "3589  3590.0  S0094     yeah that's the only one that like makes sense   \n",
              "3590  3591.0  S0021  well I use gib in a very different like meanin...   \n",
              "3591  3592.0  S0032                           what meaning do you use?   \n",
              "3592  3593.0  S0021                       well we sort of just say gib   \n",
              "\n",
              "     exactage age1994 agerange  \n",
              "0          27   25_34    19_29  \n",
              "1          28   25_34    19_29  \n",
              "2          33   25_34    30_39  \n",
              "3          33   25_34    30_39  \n",
              "4          41   35_44    40_49  \n",
              "...       ...     ...      ...  \n",
              "3588       47   45_59    40_49  \n",
              "3589       23   15_24    19_29  \n",
              "3590       23   15_24    19_29  \n",
              "3591       27   25_34    19_29  \n",
              "3592       23   15_24    19_29  \n",
              "\n",
              "[2525 rows x 6 columns]"
            ]
          },
          "execution_count": 19,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# viewing the new dataframe made\n",
        "df_new"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "27cb5dbe",
      "metadata": {
        "id": "27cb5dbe"
      },
      "source": [
        "After creating the new dataframe, I wanted to print summary statistics for all columns together. This means that I wanted to see the values of each statistical measure (such as mean, median, and standard deviation) for each column in a tabular format. By doing this, I can quickly compare the values of each column and identify any differences or similarities between them."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "267deb9f",
      "metadata": {
        "id": "267deb9f",
        "outputId": "3bddbe5e-47b7-4c3a-da1d-c22bca2ef749"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>n</th>\n",
              "      <th>who</th>\n",
              "      <th>u</th>\n",
              "      <th>exactage</th>\n",
              "      <th>age1994</th>\n",
              "      <th>agerange</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>2525.000000</td>\n",
              "      <td>2525.000000</td>\n",
              "      <td>2525.000000</td>\n",
              "      <td>2525.000000</td>\n",
              "      <td>2525.000000</td>\n",
              "      <td>2525.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>5.696238</td>\n",
              "      <td>5.092673</td>\n",
              "      <td>24.012277</td>\n",
              "      <td>1.959604</td>\n",
              "      <td>5.086733</td>\n",
              "      <td>4.943366</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.524372</td>\n",
              "      <td>0.551009</td>\n",
              "      <td>26.864813</td>\n",
              "      <td>0.293808</td>\n",
              "      <td>0.503555</td>\n",
              "      <td>0.231187</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>3.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>4.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>5.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>5.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>6.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>15.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>5.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>6.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>33.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>5.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>6.000000</td>\n",
              "      <td>9.000000</td>\n",
              "      <td>206.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>6.000000</td>\n",
              "      <td>5.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                 n          who            u     exactage      age1994  \\\n",
              "count  2525.000000  2525.000000  2525.000000  2525.000000  2525.000000   \n",
              "mean      5.696238     5.092673    24.012277     1.959604     5.086733   \n",
              "std       0.524372     0.551009    26.864813     0.293808     0.503555   \n",
              "min       3.000000     5.000000     1.000000     1.000000     4.000000   \n",
              "25%       5.000000     5.000000     4.000000     2.000000     5.000000   \n",
              "50%       6.000000     5.000000    15.000000     2.000000     5.000000   \n",
              "75%       6.000000     5.000000    33.000000     2.000000     5.000000   \n",
              "max       6.000000     9.000000   206.000000     4.000000     6.000000   \n",
              "\n",
              "          agerange  \n",
              "count  2525.000000  \n",
              "mean      4.943366  \n",
              "std       0.231187  \n",
              "min       4.000000  \n",
              "25%       5.000000  \n",
              "50%       5.000000  \n",
              "75%       5.000000  \n",
              "max       5.000000  "
            ]
          },
          "execution_count": 20,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "columns = ['n', 'who', 'u', 'exactage', 'age1994', 'agerange']\n",
        "table_data = df_new[columns].applymap(lambda x: len(str(x)))\n",
        "table_data[columns].describe()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "f98e08c8",
      "metadata": {
        "id": "f98e08c8"
      },
      "source": [
        "from the above tabular data we can extract that the average utterance is 24.012277"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "a2b829fb",
      "metadata": {
        "id": "a2b829fb"
      },
      "source": [
        "# Graphs are made for visualization of the new data"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "7486396d",
      "metadata": {
        "id": "7486396d"
      },
      "outputs": [],
      "source": [
        "# Split age range column into min and max age columns\n",
        "df_new[['min_age', 'max_age']] = df_new['agerange'].str.split('_', expand=True)\n",
        "\n",
        "# Convert age columns to integer data type\n",
        "df_new['exactage'] = pd.to_numeric(df_new['exactage'], errors='coerce')\n",
        "df_new['min_age'] = pd.to_numeric(df_new['min_age'], errors='coerce')\n",
        "df_new['max_age'] = pd.to_numeric(df_new['max_age'], errors='coerce')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1eb114d9",
      "metadata": {
        "id": "1eb114d9",
        "outputId": "22017381-bdc6-426b-e9e3-fe608ec9fd6a"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        },
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Create histogram of exact age\n",
        "df_new['exactage'].plot.hist()\n",
        "plt.show()\n",
        "# Create histogram of age range\n",
        "df_new['min_age'].plot.hist()\n",
        "df_new['max_age'].plot.hist()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "dd73b744",
      "metadata": {
        "scrolled": true,
        "id": "dd73b744",
        "outputId": "bd580136-6835-46e7-f2e6-2dbc27f689cd"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# In this bar chart it is made to show the number of speakers within the age range\n",
        "age_range_counts = df_new['agerange'].value_counts()\n",
        "plt.bar(age_range_counts.index, age_range_counts.values)\n",
        "plt.xlabel('Age Range')\n",
        "plt.ylabel('Count')\n",
        "plt.title('Count of Speakers by Age Range')\n",
        "plt.show()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "9e91fcc0",
      "metadata": {
        "id": "9e91fcc0",
        "outputId": "e2aa1a87-e26e-4611-c409-e47480d71e7c"
      },
      "outputs": [
        {
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAmoAAAHICAYAAAD+7sYHAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAzIklEQVR4nO3deZglZX33//dH9lUwjAYYFERcgCiEgaBo4hYhGoMaF9xAQ8QYN4xLxOSnaB6SPMYtaNTgCooL7qAi4i7KNiCyyk8iKCMEcAFGUZTx+/xR1XBmON3Tg3O67ul+v66rrz7nrlN1vl3T0/3pe6lKVSFJkqT23GnoAiRJkjSeQU2SJKlRBjVJkqRGGdQkSZIaZVCTJElqlEFNkiSpUQY1SauV5OQkhwxdx0KT5OlJvrgWj3dRkof2j49M8sG1eOxXJXn32jqepE68jpo0vyS5AtgEuGdV/bJv+1vgGVX10FnsfyRwr6p6xgTLnHqvAnapqssm/V6tSfJ+4GnAzX3TD4GTgH+vqhvuwLGWVdU/r8E+R3IH/537sPfBqlq8pvtKWjP2qEnz0/rAi4cuQqv1+qraAlgEPBvYF/hWks3W5pskWX9tHk/S3DGoSfPTfwAvS7LVuI1J/jPJlUluTHJOkof07QcArwKekuQXSb7bt38tyd8m2SjJ9Ul2HznWoiS/SnLX/vlfJjmvf923k9x/TYtPsnOSryT5aZKfJDl+9GtJckWSlyU5P8kNST6aZOOR7a9IcnWSq/q6K8m9Rr+Wkdc+K8lpqzs3/bZNkhyb5OdJLunfZ9nI9u2SfCLJdUkuT/Ki2Xy9VfXrqjob+CvgD+hC20q1pfPmJNf2X/P5SXZPchjwdOAV/b/ZSSPn6B+TnA/8Msn6fdsjR9564/7cLU9ybpIHjHwtt56z/vn7k/yfPkSeDGzXv98v+q97paHUJH/VD7Ve35/z+83230/SbQxq0vy0FPga8LJptp8N7AHcBfgQ8LEkG1fVF4B/BT5aVZtX1QNGd6qqm4FPAk8daX4y8PWqujbJHwPvBZ5LFzj+GzgxyUZrWH+AfwO2A+4H7AAcucprngwcAOwE3B94FtwaNv8BeCRwL+DP1vC9x56bfttrgB2BewJ/Dtw6bJjkTnRDl98FtgceARyeZP/ZvnFVLQdOBR4yZvOjgD8F7g1sBTwF+GlVHQMcT9c7t3lVPXZkn6cCjwG2qqpbxhzzQOBjI1/rp5NssJoafwn8BXBV/36bV9VVo69Jcm/gw8DhdL2FnwdOSrLhyMvG/vtJWplBTZq/Xg28MMmiVTdU1Qer6qdVdUtVvRHYCLjPLI/7IVYOak/r2wCeA/x3VZ1ZVSuq6li6OVj7rknhVXVZVZ1aVTdX1XXAm7h94Dq6qq6qqp/RBaQ9+vYnA++rqouq6ibgtWv43jOdmycD/1pVP6+qZcDRI7vuDSyqqtdV1W+q6gfAu4CD1uT9gavogtOqfgtsAdyXbn7xJVV19WqOdXRVXVlVv5pm+zlV9fGq+i3dOd6YNfy3msZTgM/1/4a/Bd5AN2/yQavUNu7fT9IIg5o0T1XVhcBngVeuui3JS/uhuxuSXA/cGdhmlof+CrBJkj9Jcg+6X7Cf6rfdA3hpP9x1fX/sHeh6xmYtyV2TfCTJj5PcCHxwTH3/O/L4JmDz/vF2wJUj20Yfz+a9Zzo3Mx37HnTDgaNf+6uAu63J+9P1xv1s1caq+grwNuC/gGuSHJNky9Uca3Vf+63bq+p3wDLW8N9qGtvRLY4YPfaVdF/blOn+/SSNMKhJ89tr6Hq5bv0F2c+5+ke63qGtq2or4Aa64UaAGZeC9790T6DrVXsa8Nl+yA66X8ZHVdVWIx+bVtWH17Duf+vruH9VbUk3xJiZd7nV1cDoasQdVtn+S2DTked/OPVgFudmpmNfCVy+yte+RVU9epZ1k2RzuiHbb47bXlVHV9VewG50Q6Avn9o0zSFXt6z/1vr7odvFdD160IWnsedpFse9ii64Th07/Xv9eDX7SVqFQU2ax/rLXnwUGJ3UvgVwC3AdsH6SVwOjPTPXADv2v7in8yG64a2nc9uwJ3RDfX/X97YlyWZJHpNkixmOtWGSjUc+1utr/AVwfZLtuS2QzMYJwLOT3C/JpnRDwKPOA56QZNN+svyhI9tWd25OAI5IsnVf1wtGtp0F3NhP4N8kyXr9ZP+9V1dwukUaewGfBn4OvG/Ma/buz+sGdGHz18CKfvM1dPPm1tReSZ6QblXo4XTD1Gf0284DntZ/HQew8tDzNcAfJLnzNMc9AXhMkkf09b60P/a370CN0oJmUJPmv9cBo5d7OIVu1d7/Tzc89WtWHiL7WP/5p0nOHXfAqjqTLixs1x9rqn0pXQ/e2+gCx2WsfpL4RcCvRj6eTTev7I/perM+R7eAYVaq6mS6uWNf7d//9H7T1PXK3gz8hi5sHEs3EX/K6s7N6+iGBy8HvgR8fOq4VbUCeCzdUPDlwE+Ad9MNnU7nFUmW0w11HgecAzxo6vp3q9iSLgj/vK/tp3RzvwDeA+zaD7l+eob3W9Vn6AL3z4FnAk/o55RBd3mXxwLX0wXyW49bVd+jWyzwg/49VxourapL6XpB30p3Hh4LPLaqfrMGtUnCC95Kmuf6y0JcCGw0zcrH3+fYzwMOqqo1XVkqSbNij5qkeSfJ45NsmGRr4P8CJ62NkJZk2yT7JblTkvvQDel9anX7SdIdZVCTNB89l26e2f/QzeN63lo67oZ014ZbTrf69TPA29fSsSXpdhz6lCRJapQ9apIkSY0yqEmSJDVq/aELmJRtttmmdtxxx6HLkCRJWq1zzjnnJ1V1u1v+zdugtuOOO7J06dKhy5AkSVqtJD8c1+7QpyRJUqMMapIkSY0yqEmSJDXKoCZJktQog5okSVKjDGqSJEmNMqhJkiQ1yqAmSZLUKIOaJElSowxqkiRJjTKoSZIkNWpiQS3JxknOSvLdJBcleW3ffmSSHyc5r/949Mg+RyS5LMmlSfYfad8ryQX9tqOTZFJ1S5IktWKSN2W/GXh4Vf0iyQbAaUlO7re9uareMPriJLsCBwG7AdsBX0py76paAbwDOAw4A/g8cABwMpIkSfPYxIJaVRXwi/7pBv1HzbDLgcBHqupm4PIklwH7JLkC2LKqTgdIchzwOH6PoLbXy4+7o7s275z/OHjoEiRJ0loy0TlqSdZLch5wLXBqVZ3Zb3pBkvOTvDfJ1n3b9sCVI7sv69u27x+v2i5JkjSvTTSoVdWKqtoDWEzXO7Y73TDmzsAewNXAG/uXj5t3VjO0306Sw5IsTbL0uuuu+z2rlyRJGtacrPqsquuBrwEHVNU1fYD7HfAuYJ/+ZcuAHUZ2Wwxc1bcvHtM+7n2OqaolVbVk0aJFa/eLkCRJmmOTXPW5KMlW/eNNgEcC30uy7cjLHg9c2D8+ETgoyUZJdgJ2Ac6qqquB5Un27Vd7Hgx8ZlJ1S5IktWKSqz63BY5Nsh5dIDyhqj6b5ANJ9qAbvrwCeC5AVV2U5ATgYuAW4Pn9ik+A5wHvBzahW0Tgik9JkjTvTXLV5/nAnmPanznDPkcBR41pXwrsvlYLlCRJapx3JpAkSWqUQU2SJKlRBjVJkqRGGdQkSZIaZVCTJElqlEFNkiSpUQY1SZKkRhnUJEmSGmVQkyRJapRBTZIkqVEGNUmSpEYZ1CRJkhplUJMkSWqUQU2SJKlRBjVJkqRGGdQkSZIaZVCTJElqlEFNkiSpUQY1SZKkRhnUJEmSGmVQkyRJapRBTZIkqVEGNUmSpEYZ1CRJkhplUJMkSWqUQU2SJKlRBjVJkqRGGdQkSZIaZVCTJElqlEFNkiSpUQY1SZKkRhnUJEmSGmVQkyRJapRBTZIkqVEGNUmSpEZNLKgl2TjJWUm+m+SiJK/t2++S5NQk3+8/bz2yzxFJLktyaZL9R9r3SnJBv+3oJJlU3ZIkSa2YZI/azcDDq+oBwB7AAUn2BV4JfLmqdgG+3D8nya7AQcBuwAHA25Os1x/rHcBhwC79xwETrFuSJKkJEwtq1flF/3SD/qOAA4Fj+/Zjgcf1jw8EPlJVN1fV5cBlwD5JtgW2rKrTq6qA40b2kSRJmrcmOkctyXpJzgOuBU6tqjOBu1XV1QD957v2L98euHJk92V92/b941XbJUmS5rWJBrWqWlFVewCL6XrHdp/h5ePmndUM7bc/QHJYkqVJll533XVrXK8kSVJL5mTVZ1VdD3yNbm7ZNf1wJv3na/uXLQN2GNltMXBV3754TPu49zmmqpZU1ZJFixatzS9BkiRpzk1y1eeiJFv1jzcBHgl8DzgROKR/2SHAZ/rHJwIHJdkoyU50iwbO6odHlyfZt1/tefDIPpIkSfPW+hM89rbAsf3KzTsBJ1TVZ5OcDpyQ5FDgR8CTAKrqoiQnABcDtwDPr6oV/bGeB7wf2AQ4uf+QJEma1yYW1KrqfGDPMe0/BR4xzT5HAUeNaV8KzDS/TZIkad7xzgSSJEmNMqhJkiQ1yqAmSZLUKIOaJElSowxqkiRJjTKoSZIkNcqgJkmS1CiDmiRJUqMMapIkSY0yqEmSJDXKoCZJktQog5okSVKjDGqSJEmNMqhJkiQ1yqAmSZLUKIOaJElSowxqkiRJjTKoSZIkNcqgJkmS1CiDmiRJUqMMapIkSY0yqEmSJDXKoCZJktQog5okSVKjDGqSJEmNMqhJkiQ1yqAmSZLUKIOaJElSowxqkiRJjTKoSZIkNcqgJkmS1CiDmiRJUqMMapIkSY0yqEmSJDXKoCZJktSoiQW1JDsk+WqSS5JclOTFffuRSX6c5Lz+49Ej+xyR5LIklybZf6R9ryQX9NuOTpJJ1S1JktSK9Sd47FuAl1bVuUm2AM5Jcmq/7c1V9YbRFyfZFTgI2A3YDvhSkntX1QrgHcBhwBnA54EDgJMnWLskSdLgJtajVlVXV9W5/ePlwCXA9jPsciDwkaq6uaouBy4D9kmyLbBlVZ1eVQUcBzxuUnVLkiS1Yk7mqCXZEdgTOLNvekGS85O8N8nWfdv2wJUjuy3r27bvH6/aLkmSNK9NPKgl2Rz4BHB4Vd1IN4y5M7AHcDXwxqmXjtm9Zmgf916HJVmaZOl11133+5YuSZI0qIkGtSQb0IW046vqkwBVdU1Vraiq3wHvAvbpX74M2GFk98XAVX374jHtt1NVx1TVkqpasmjRorX7xUiSJM2xSa76DPAe4JKqetNI+7YjL3s8cGH/+ETgoCQbJdkJ2AU4q6quBpYn2bc/5sHAZyZVtyRJUismuepzP+CZwAVJzuvbXgU8NckedMOXVwDPBaiqi5KcAFxMt2L0+f2KT4DnAe8HNqFb7emKT0mSNO9NLKhV1WmMn1/2+Rn2OQo4akz7UmD3tVedJElS+7wzgSRJUqMMapIkSY0yqEmSJDXKoCZJktQog5okSVKjDGqSJEmNMqhJkiQ1yqAmSZLUKIOaJElSowxqkiRJjTKoSZIkNcqgJkmS1CiDmiRJUqMMapIkSY0yqEmSJDXKoCZJktQog5okSVKjDGqSJEmNMqhJkiQ1yqAmSZLUKIOaJElSowxqkiRJjTKoSZIkNcqgJkmS1CiDmiRJUqMMapIkSY0yqEmSJDXKoCZJktQog5okSVKjDGqSJEmNMqhJkiQ1yqAmSZLUKIOaJElSowxqkiRJjTKoSZIkNcqgJkmS1KiJBbUkOyT5apJLklyU5MV9+12SnJrk+/3nrUf2OSLJZUkuTbL/SPteSS7otx2dJJOqW5IkqRWT7FG7BXhpVd0P2Bd4fpJdgVcCX66qXYAv98/ptx0E7AYcALw9yXr9sd4BHAbs0n8cMMG6JUmSmjCxoFZVV1fVuf3j5cAlwPbAgcCx/cuOBR7XPz4Q+EhV3VxVlwOXAfsk2RbYsqpOr6oCjhvZR5Ikad6akzlqSXYE9gTOBO5WVVdDF+aAu/Yv2x64cmS3ZX3b9v3jVdvHvc9hSZYmWXrdddet1a9BkiRprs0qqCXZbzZt0+y7OfAJ4PCqunGml45pqxnab99YdUxVLamqJYsWLZpNeZIkSc2abY/aW2fZtpIkG9CFtOOr6pN98zX9cCb952v79mXADiO7Lwau6tsXj2mXJEma19afaWOSBwIPAhYl+YeRTVsC643f69Z9A7wHuKSq3jSy6UTgEODf+8+fGWn/UJI3AdvRLRo4q6pWJFmeZF+6odODmUVIlCRJWtfNGNSADYHN+9dtMdJ+I/DE1ey7H/BM4IIk5/Vtr6ILaCckORT4EfAkgKq6KMkJwMV0K0afX1Ur+v2eB7wf2AQ4uf+QJEma12YMalX1deDrSd5fVT9ckwNX1WmMn18G8Ihp9jkKOGpM+1Jg9zV5f0mSpHXd6nrUpmyU5Bhgx9F9qurhkyhKkiRJsw9qHwPeCbwbWLGa10qSJGktmG1Qu6Wq3jHRSiRJkrSS2V6e46Qkf59k2/5enXdJcpeJViZJkrTAzbZH7ZD+88tH2gq459otR5IkSVNmFdSqaqdJFyJJkqSVzSqoJTl4XHtVHbd2y5EkSdKU2Q597j3yeGO666CdCxjUJEmSJmS2Q58vHH2e5M7AByZSkSRJkoDZr/pc1U109+KUJEnShMx2jtpJdKs8obsZ+/2AEyZVlCRJkmY/R+0NI49vAX5YVcsmUI8kSZJ6sxr67G/O/j1gC2Br4DeTLEqSJEmzDGpJngycBTwJeDJwZpInTrIwSZKkhW62Q5//BOxdVdcCJFkEfAn4+KQKkyRJWuhmu+rzTlMhrffTNdhXkiRJd8Bse9S+kOQU4MP986cAn59MSZIkSYLVBLUk9wLuVlUvT/IE4MFAgNOB4+egPkmSpAVrdcOXbwGWA1TVJ6vqH6rqJXS9aW+ZbGmSJEkL2+qC2o5Vdf6qjVW1FNhxIhVJkiQJWH1Q23iGbZuszUIkSZK0stUFtbOTPGfVxiSHAudMpiRJkiTB6ld9Hg58KsnTuS2YLQE2BB4/wbokSZIWvBmDWlVdAzwoycOA3fvmz1XVVyZemSRJ0gI3q+uoVdVXga9OuBZJkiSN8O4CkiRJjTKoSZIkNcqgJkmS1CiDmiRJUqMMapIkSY0yqEmSJDXKoCZJktQog5okSVKjDGqSJEmNMqhJkiQ1amJBLcl7k1yb5MKRtiOT/DjJef3Ho0e2HZHksiSXJtl/pH2vJBf0245OkknVLEmS1JJJ9qi9HzhgTPubq2qP/uPzAEl2BQ4Cduv3eXuS9frXvwM4DNil/xh3TEmSpHlnYkGtqr4B/GyWLz8Q+EhV3VxVlwOXAfsk2RbYsqpOr6oCjgMeN5GCJUmSGjPEHLUXJDm/Hxrdum/bHrhy5DXL+rbt+8erto+V5LAkS5Msve6669Z23ZIkSXNqroPaO4CdgT2Aq4E39u3j5p3VDO1jVdUxVbWkqpYsWrTo9yxVkiRpWHMa1KrqmqpaUVW/A94F7NNvWgbsMPLSxcBVffviMe2SJEnz3pwGtX7O2ZTHA1MrQk8EDkqyUZKd6BYNnFVVVwPLk+zbr/Y8GPjMXNYsSZI0lPUndeAkHwYeCmyTZBnwGuChSfagG768AnguQFVdlOQE4GLgFuD5VbWiP9Tz6FaQbgKc3H9IkiTNexMLalX11DHN75nh9UcBR41pXwrsvhZLkyRJWid4ZwJJkqRGGdQkSZIaZVCTJElqlEFNkiSpUQY1SZKkRhnUJEmSGmVQkyRJapRBTZIkqVEGNUmSpEYZ1CRJkhplUJMkSWqUQU2SJKlRBjVJkqRGGdQkSZIaZVCTJElqlEFNkiSpUQY1SZKkRhnUJEmSGmVQkyRJapRBTZIkqVEGNUmSpEYZ1CRJkhplUJMkSWqUQU2SJKlRBjVJkqRGGdQkSZIaZVCTJElqlEFNkiSpUQY1SZKkRhnUJEmSGmVQkyRJapRBTZIkqVEGNUmSpEYZ1CRJkhplUJMkSWrUxIJakvcmuTbJhSNtd0lyapLv95+3Htl2RJLLklyaZP+R9r2SXNBvOzpJJlWzJElSSybZo/Z+4IBV2l4JfLmqdgG+3D8nya7AQcBu/T5vT7Jev887gMOAXfqPVY8pSZI0L00sqFXVN4CfrdJ8IHBs//hY4HEj7R+pqpur6nLgMmCfJNsCW1bV6VVVwHEj+0iSJM1rcz1H7W5VdTVA//muffv2wJUjr1vWt23fP161XZIkad5rZTHBuHlnNUP7+IMkhyVZmmTpddddt9aKkyRJGsJcB7Vr+uFM+s/X9u3LgB1GXrcYuKpvXzymfayqOqaqllTVkkWLFq3VwiVJkubaXAe1E4FD+seHAJ8ZaT8oyUZJdqJbNHBWPzy6PMm+/WrPg0f2kSRJmtfWn9SBk3wYeCiwTZJlwGuAfwdOSHIo8CPgSQBVdVGSE4CLgVuA51fViv5Qz6NbQboJcHL/IUmSNO9NLKhV1VOn2fSIaV5/FHDUmPalwO5rsTRJkqR1QiuLCSRJkrQKg5okSVKjDGqSJEmNMqhJkiQ1yqAmSZLUKIOaJElSowxqkiRJjTKoSZIkNcqgJkmS1CiDmiRJUqMMapIkSY0yqEmSJDXKoCZJktQog5okSVKjDGqSJEmNMqhJkiQ1yqAmSZLUKIOaJElSowxqkiRJjTKoSZIkNcqgJkmS1CiDmiRJUqMMapIkSY0yqEmSJDXKoCZJktQog5okSVKjDGqSJEmNMqhJkiQ1yqAmSZLUKIOaJElSowxqkiRJjTKoSZIkNcqgJkmS1CiDmiRJUqMMapIkSY0aJKgluSLJBUnOS7K0b7tLklOTfL//vPXI649IclmSS5PsP0TNkiRJc23IHrWHVdUeVbWkf/5K4MtVtQvw5f45SXYFDgJ2Aw4A3p5kvSEKliRJmkstDX0eCBzbPz4WeNxI+0eq6uaquhy4DNhn7suTJEmaW0MFtQK+mOScJIf1bXerqqsB+s937du3B64c2XdZ3yZJkjSvrT/Q++5XVVcluStwapLvzfDajGmrsS/sQt9hAHe/+91//yolSZIGNEiPWlVd1X++FvgU3VDmNUm2Beg/X9u/fBmww8jui4GrpjnuMVW1pKqWLFq0aFLlS5IkzYk5D2pJNkuyxdRj4FHAhcCJwCH9yw4BPtM/PhE4KMlGSXYCdgHOmtuqJUmS5t4QQ593Az6VZOr9P1RVX0hyNnBCkkOBHwFPAqiqi5KcAFwM3AI8v6pWDFC3JEnSnJrzoFZVPwAeMKb9p8AjptnnKOCoCZcmSZLUlJYuzyFJkqQRBjVJkqRGGdQkSZIaZVCTJElqlEFNkiSpUQY1SZKkRhnUJEmSGmVQkyRJapRBTZIkqVEGNUmSpEYZ1CRJkhplUJMkSWqUQU2SJKlRBjVJkqRGGdQkSZIaZVCTJElqlEFNkiSpUQY1SZKkRhnUJEmSGmVQkyRJapRBTZIkqVEGNUmSpEYZ1CRJkhplUJMkSWqUQU2SJKlRBjVJkqRGGdQkSZIaZVCTJElqlEFNkiSpUQY1SZKkRhnUJEmSGmVQkyRJapRBTZIkqVEGNUmSpEYZ1CRJkhq1zgS1JAckuTTJZUleOXQ9kiRJk7b+0AXMRpL1gP8C/hxYBpyd5MSqunjYyuaPH73uj4YuYaLu/uoLhi5BkqQ1tk4ENWAf4LKq+gFAko8ABwIGNU3Ufm/db+gSJupbL/zW0CVIkmawrgS17YErR54vA/5koFokSbN01DOeOHQJE/VPH/z40CVonktVDV3DaiV5ErB/Vf1t//yZwD5V9cJVXncYcFj/9D7ApXNa6PS2AX4ydBGN8ZyM53kZz/Mynufl9jwn43lexmvpvNyjqhat2riu9KgtA3YYeb4YuGrVF1XVMcAxc1XUbCVZWlVLhq6jJZ6T8Twv43lexvO83J7nZDzPy3jrwnlZV1Z9ng3skmSnJBsCBwEnDlyTJEnSRK0TPWpVdUuSFwCnAOsB762qiwYuS5IkaaLWiaAGUFWfBz4/dB13UHPDsQ3wnIzneRnP8zKe5+X2PCfjeV7Ga/68rBOLCSRJkhaidWWOmiRJ0oJjUJMkSWqUQU2SJKlR68xiAklaqJLct6q+l+SPx22vqnPnuqbW9PeEvhsjv9eq6kfDVTSsJJsCLwXuXlXPSbILcJ+q+uzApQ0iyWlV9eAky4HRyfkBqqq2HKi01XIxwYQk2Qj4a2BHVv7B8bqhampBkgdx+3Ny3GAFDSjJBaz8A2MlVXX/OSynSX6/dJIcU1WHJfnqmM1VVQ+f86IakuSFwGuAa4Df9c21kP8PJfkocA5wcFXtnmQT4PSq2mPYyrSm7FGbnM8AN9D9R7l54FqakOQDwM7AecCKvrmABfeLt/eX/efn958/0H9+OnDT3JfTFr9fblNVU7fG+4uq+vXotiQbD1BSa15M11v006ELacjOVfWUJE8FqKpfJcnQRbVgXet9NahNzuKqOmDoIhqzBNi17MYFoKp+CJBkv6rab2TTK5N8C1jQva/4/TLOt4FVhz/HtS00V9L9Yazb/KbvRSuAJDtjp8G0va9As72vBrXJ+XaSP6qqC4YupCEXAn8IXD10IY3ZLMmDq+o0uHW4b7OBa2qB3y+9JH8IbA9skmRPunk1AFsCmw5WWDt+AHwtyecYCSNV9abhShrca4AvADskOR7YD3jWoBW1YZ3rfTWorWUj847WB56d5Ad0PzimJiw2m9onJclJdOdkC+DiJGex8g/TvxqqtkYcCrw3yZ3759cDfzNcOc3YBr9fpuxP90t2MTAaPpYDrxqioMb8qP/YsP9Y8Krq1CTnAvvS/f55cVX9ZOCyWrDO9b66mGAtS3KPmbZPDXctJEn+bKbtVfX1uaqlZUm2pPs/uU79EJmU6b5vFvL3S5K/rqpPDF2H2pdkP+C8qvplkmfQDY//50L8HTQqyXuA+wDrTO+rQW1C+vkAy6rq5iQPpRv/Pq6qrh+yriEl2Qz4VVX9Lsm9gfsCJ1fVbwcubVCuENaaSPIYYDfg1kUEC/17Jcki4BXc/rws2NWwSc4HHkD/uwd4L/CEqprxD+f5LslrxrVX1WvnupbZcuhzcj4BLElyL+A9wInAh4BHD1rVsL4BPCTJ1sCXgaXAU+hWOS5krhAeI8m+wFuB+9ENZ60H/LLl6x1NWpJ30s1JexjwbuCJwFmDFtWG44GP0q2k/jvgEOC6QSsa3i1VVUkOBI6uqvckOWTooobWciCbjkFtcn5XVbckeQLwlqp6a5LvDF3UwFJVNyU5FHhrVb0+yXlDF9UAVwiP9zbgIOBjdCtADwZ2GbSi4T2oqu6f5Pyqem2SNwKfHLqoBvxBH0Re3A+Nfz3Jgh0i7y1PcgTwTLo/kNcDNhi4psGti72v3kJqcn7bX7/mYGDqStAL/T9JkjyQrgftc33begPW04pvJ/mjoYtoUVVdBqxXVSuq6n3AQwcuaWhT11C7Kcl2wG+BnQaspxVT0yeuTvKYfmXs4iELasBT6Hro/6aq/pdu1fB/DFtSE44Hvkf3/+a1wBXA2UMWtDr2qE3Os+m64I+qqsuT7AR8cOCahnY4cATwqaq6KMk9gXFXWl9oHgw8K8nlLPAVwqu4KcmGwHlJXk93mY6FftmSk5JsRfcL91y61dTvGrSiNvyfftX0S+mGy7cEXjJsScOqqv9N8glu64X+CfCpAUtqxTrX++piAmlg060UdnVW7gFcS9cT/RLgzsDb+162BSfJnYB9q+rb/fONgI1dJaxxkjwHOAy4S1Xt3N/r851V9YiBSxtUkjOqat8kpwBHA1cBH6+qnQcubVoGtbUsyQlV9eTp7uO4EHtJkrylqg4fuZ7aShbodbFuJ8ldWXnORLO3NNEwkpxeVQ8cuo7W9CMWL+T2K6cX7M+Wfv7vPsCZVbVn33ZBVS3oaRZJ/hL4JrADt/W+vraqThy0sBk49Ln2vbj//JczvmphmbqH5RsGraJRSf4KeCOwHV0P0j2AS+gmuy44/rEzoy8m+Wvgk95aayWfpltdfxK33RZoobu5qn4zdXvPJOsz5v/TQtIvqNilqj5Lt9L+YQOXNCv2qGnO9HMC/nN1bQtNku8CDwe+VFV7JnkY8NSRG3EvKEm2raqrHRK+vSTL6ebp3UK3sGBqPuOCvWQJQJIzq+pPhq6jJf28zuvpFrS9EPh74OKq+qch6xpakq9W1ToR0KYY1Nay/gfpuJO64H+gJjm3qv54lbbvTHXLL1RJllbVkj6w7dlfEPisqtpn6NqG0v/le0pVPXLoWtS+JE+jmzT/RVa+2vy5gxU1sH5O46HAo+h+/5wCvHuh98QmOYpuvutHgV9Otbf8veLQ51pWVVsMXUNr+suUPA3YKcnoPIAtgHXmxrgTdH2SzekuCHx8kmvpekwWrKpakeSmJHd2svzK+gtG78LK8xm/MVxFTfgjuuuFPZzbhj6rf74gVdXv6FYEuyp4ZQ/qP4/ezaPp7xV71CYkyV3GNC9fiLdL6oewdgL+DXjlyKblwPlVtaBDSX9rralhrKfT/bV3fFUt6BCb5AS6G0qfysp/+b5osKIGluRv6ebBLgbOozs/p7d8sc65kOR7wP2r6jdD19KK/l6fR9LNeV2f20Z17jlkXVpzBrUJSXIF3aqSn9P9B9mK7jpQ1wLPqapzBitOWgdMd7ubqjp2rmtpRb/AYm/gjKraI8l96VasPWXg0gaV5KPAC6vq2qFraUUfXl9Cd2u6FVPt/gGYOwOvAf60b/o68LqWe+4d+pycL9Bd2PUUgCSPAg4ATgDeDiyYia9JTquqB4+Zv7eg5+05n3FmCzmQzeDXVfXrJCTZqKq+l+Q+QxfVgLsB30tyNivPUVuwl+cAbqiqk4cuokHvBS4Entw/fybwPuAJg1W0GvaoTcjUBPFxbUnOq6o9BipNWif0F+j8N2BXVp6PtWCHbpJ8iu6uJ4fTzan5ObBBVT16yLqGluTPxrX3V55fkJL8O90t+j6JCyxuNe73b+u/k+1Rm5yfJflH4CP986cAP+9Xsy246/z0K5DOr6rdh66lNc5nnNb76IYo3kx3vaNn0/U2LlhV9fj+4ZFJvko3n/ELA5Y0uP5ny3/5s+V2pkZtRjsMmp40P0d+leTBVXUa3DqX71cD1zQje9QmJMk2dL9kHkz3y+U0uhvA3gDcfSHeBifJ8cARXnF/Zc5nHC/JOVW11+jV1JN8s6oeMnRtcy3JllV14zShvoAbq2rFmG0Lgj9bNFtJHgAcR/dHToCfAc+qqu8OWtgM7FGbkKr6Cd1FBsdZcCGtty1wUZKzWHkV30KeRwLOZ5zOr/veku8neQHwY+CuA9c0lA/R3e3kHLpgtmrP4uZJ3lVVr5rzytrgz5YxkjyG7g4no1MHXjf9HvNfH8gekGTL/vmNA5e0WvaoTUiSewMv4/b3nluw3c7OIxnP+YzjJdmb7lZaWwH/QvcX8Our6owh62pRP6Xiwqq639C1DMGfLbeX5J3ApnTTBt4NPBE4q6oOHbSwgSR5LN30mx/2z18N/DXwQ+DFVXX5kPXNxKA2If1V5t/J7ZdGL8hhrFX1Q8M/XehXyQZI8kXgy6w8n/HP6XrVzl71bg5auJL86bh2L3h76/Uad6mqLyXZFFivqpYPXddQkpxfVfcf+bw53T1iHzV0bUNIcj6wb1Xd1N+Y/U3AU4E9gSdV1f6DFjgDhz4n55aqesfQRbQgyb7Av9PNBfgXupu0bwPcKcnBVbWgJ0PT3bXhNXQ3lp6az/g0uhVbT55+t/ktyUnc/vIlNwBLgf+uql/PfVWDe/nI442Bfej+GFywPfUASZ4DHAbcBdgZ2J7uD+VHDFnXwKYmyN+UZDu6u8DsNGA9Q6uquql//ATgPX3HyTlJ/n7AulbLoDY5J/X/+J9i5aXRPxuupMG8DXgV3dDVV4C/qKoz+ot1fpgFvmrN+YzT+gGwiO57BLqexmuAe9PdFueZA9U1mKp67OjzJDsArx+onJY8ny60nglQVd9PslDnM075bJKtgP8AzqX7o2ch304qfa/iTXQB/u0j2zYev0sbDGqTM3VV9dG/gAtYiNeAWr+qvgiQ5HVTc4z6i3UOW1kDnM84rT2ranSo76Qk36iqP01y0WBVtWUZ4GUp4Oaq+s3Uz5Mk6zP+YtILRlX9S//wE0k+C2zc8tX358Bb6G67diNwSVUtBUiyJ90q+2YZ1CakqhZyF/OqRq8bt+r1ahb0D9Pex+iGad7NyHxGsSjJ3acuuZDk7nRD5gAL8p6OSd7Kbf9n7kQ3v6bZywrMoa8neRWwSZI/B/4eOGngmgaVZGO68/Bguu+Z05K8Y4FOGaCq3pvkFLqV46P/Z/6X7hqNzXIxwVqW5BVV9fr+8ZOq6mMj2/51IS6fT7KCbsl8gE3oup7pn29cVRsMVVsLpq4XNnQdrUnyaLoA+z903ys70f3i+Rrd9eXeMlhxAxm5/2kBtwBXVNW3ByypCf1lXA4FpibKn1JV7x6wpMElOQFYDnywb3oqsHVVPWm4qnRHGNTWsiTnTq3SG3087rkEkORIuovbOp9xFUk2Au5LF9S+t1B7A5IcCCyuqv/qn59FN3+vgFdU1ceHrG8onpfpJfluVT1gdW1qn0Ofa1+meTzuuQTOZ5zJXtw2d+/+Saiq44YtaRCvAA4aeb4h3bnZnO5WWws1kHhepvedJPtOzQlO8ifAtwauSXeAQW3tq2kej3suOZ9xGkk+QHephfO4be5e0d3+ZaHZsKquHHl+Wt/j+rMkmw1VVAM8L9P7E+DgJFO31bo7cEmSC+guVXH/4UprQ5LDquqYoetYHYc+1zLnY2m2nM84sySXALt6UWRIcllV3Wuabf9TVTvPdU0t8LxMr78A8LSmrtC/kK0r05HuNHQB801VrVdVW1bVFlW1fv946rkhTaNGh2yOWGXbAXNZSKMuBP5w6CIacWZ/UdeVJHkucNYA9bTC8zKNqvphH8Z+RdcTXV3zre1aR6YjOfQpDcf5jDPbBri4nyA+ushiId5o+yXAp5M8je7ipdDNxdoIeNxQRTXA8zKNJH8FvBHYjm6x0j3o7p2725B1Neaxq3/J8Axq0nCczzizI4cuoBVVdS3woCQP57ZftJ+rqq8MWNbgPC8z+hdgX+BLVbVnkofRXaJDvapaNnQNs+EcNWkgzmeUNClJllbVkiTfpbvLx++SnFVV+wxdm9aMPWrSQKpqvaFraFmS5dzWs7ghsAHwy6racriqpHXG9f29Lb8JHJ/kWrqLJGsdY4+apHVCkscB+yz01bDSbCTZFPg1XQ/9M4AtgeO9kDYkeRC3v7dys5f9MahJWmckOaOq9h26DqlVq/RE39rcf/413S3Z/qmqvjynhTViuuszVtWLBitqNRz6lNSkJE8YeXonYAkuspBmVFVbTLctyXrA7sDx/eeFaAnr2PUZDWqSWjW6dP4W4ArgwGFKkdZ9VbUC+G6Stw5dy4Cmrs949dCFzJZDn5IkaV5LchJdj/wWwB50F0ReJ67PaI+apKb0f+1P+xdky3NJJDXrDUMXcEcZ1CS1ZunI49cCrxmqEEnzQ1V9HSDJZsCv+uvK3Ru4L3DyoMWthkOfkpqV5DtVtefQdUiaH5KcAzwE2Bo4g+4Pw5uq6umDFjYDb8ouqWX+JSlpbUpV3QQ8AXhrVT2exu9/alCTJEkLRZI8EHg68Lm+rem7xDhHTVJTVrlg56ZJbpzaRHdhSm8hJemOOhw4AvhUVV2U5J7AV4ctaWbOUZMkSWqUPWqSJGleS/KWqjp85HpqK/E6apIkScP5QP95nbuemkOfkiRJjbJHTZIkzWtJLmDmO57cfw7LWSMGNUmSNN/9Zf/5+f3nqaHQpwM3zX05s+fQpyRJWhCSfKuq9ltdW0u84K0kSVooNkvy4KknSR4EbDZgPavl0KckSVoo/gZ4X5I7081Zu6Fva5ZBTZIkzXtJ1gP+rKoekGRLuulfNwxd1+o49ClJkua9qloBHNg/vnFdCGngYgJJkrRAJDkKuDPwUeCXU+1Vde5gRa2GQU2SJC0IScbdgL2q6uFzXswsGdQkSZIa5WICSZK0ICR59bj2qnrdXNcyWwY1SZK0UPxy5PHGdHcsuGSgWmbFoU9JkrQgJdkIOLGq9h+6lul4eQ5JkrRQbQrcc+giZuLQpyRJWhCSXEB3RwKA9YBFQLPz08CgJkmS5rkki6tqGd2ctCm3ANcAfzFMVbPjHDVJkjSvJbkU2L+qrlil/dnAP1fVzoMUNgvOUZMkSfPdS4BTk+wy1ZDkCOAfgD8brKpZcOhTkiTNa1X1+SQ3AycneRzwt8DewJ9W1c8HLW41HPqUJEkLQpIHA58Gvg08uap+PWxFq2dQkyRJ81qS5XSrPQNsBPwWWNE/r6racsDyZmRQkyRJapSLCSRJkhplUJMkSWqUQU2SJKlRBjVJTUhSSd448vxlSY5czT4PTfKgked/l+TgtVDLkUle9vseR5J+XwY1Sa24GXhCkm3WYJ+HArcGtap6Z1Udt7YLk6ShGNQkteIW4Bi6K4ivJMljk5yZ5DtJvpTkbkl2BP4OeEmS85I8ZKonLMn9kpw1sv+OSc7vH++V5OtJzklySpJtZ1tgkk/3+12U5LCR9l8kOSrJd5OckeRuffvO/fOzk7wuyS/69ocm+ezI/m9L8qz+8av711+Y5Jgk6dv3TnJ+ktOT/EeSC/v29frnZ/fbnzv7Uy6pdQY1SS35L+DpSe68SvtpwL5VtSfwEeAV/T373gm8uar2qKpvTr24qi4BNkxyz77pKcAJSTYA3go8sar2At4LHLUG9f1Nv98S4EVJ/qBv3ww4o6oeAHwDeE7f/p/Af1bV3sBVs3yPt1XV3lW1O7AJt91E+n3A31XVA+mu/zTlUOCG/j32Bp6TZKc1+JokNcygJqkZVXUjcBzwolU2LQZOSXIB8HJgt1kc7gTgyf3jpwAfBe4D7E53z7/zgH/ujz1bL0ryXeAMYAdg6r6BvwGmesjOAXbsHz8Q+Fj/+EOzfI+H9b2HFwAPB3ZLshWwRVV9e8yxHgUc3H89ZwJ/MFKXpHWc9/qU1Jq3AOfS9SBNeSvwpqo6MclDgSNncZyPAh9L8km6K49/P8kfARf1vVJrpH/fRwIPrKqbknwN2Ljf/Nu67erhK1j9z9ZbWPkP5Y3799gYeDuwpKqu7BdTbEx39fRpSwNeWFWnzPqLkbTOsEdNUlOq6md0vWGHjjTfGfhx//iQkfblwBbTHOd/6ELT/0cX2gAuBRYleSBAkg2SzKZ3bqqGn/ch7b7AvrPY5wzgr/vHB420/xDYNclG/TDvI/r2qeD3kySbA0/sv5afA8uT7DvmWKcAz+uHdUly7ySbzfJrktQ4g5qkFr0RGF39eSRd79g3gZ+MtJ8EPH5qMcGY43wUeAZd8KOqfkMXfv5vP4R5HiOrRlfxz0mWTX0AXwDW7xcl/AtdCFudw4F/6Bc2bAvc0NdxZV/T+cDxwHf69uuBdwEX0N04+uyRYx0KHJPkdLpetBv69ncDFwPn9gsM/htHS6R5w3t9StKEJNkU+FVVVZKDgKdW1YF38FibV9XUqtFXAttW1YvXYrmSGuRfXZI0OXsBb+svsXE98De/x7Eek+QIup/bPwSe9XtXJ6l59qhJkiQ1yjlqkiRJjTKoSZIkNcqgJkmS1CiDmiRJUqMMapIkSY0yqEmSJDXq/wFdRwOMq608PAAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 720x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# bar plot showing the First language count of speakers\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.countplot(x='l1', data=df_speaker)\n",
        "plt.xlabel('Native Language')\n",
        "plt.ylabel('Count')\n",
        "plt.title('Native Language Distribution')\n",
        "plt.xticks(rotation=90)\n",
        "plt.show()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "e62ccec0",
      "metadata": {
        "id": "e62ccec0",
        "outputId": "223c133e-faa9-43df-dc7c-f26142d215a2"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Making a histogram to see the difference of utterence on the region Linguistic origin\n",
        "\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.countplot(data=df_speaker, x='lingorig', order=df_speaker['lingorig'].value_counts().head(7).index)\n",
        "plt.xlabel('lingorig')\n",
        "plt.ylabel('Count')\n",
        "plt.title('Top 7 Linguistic origin')\n",
        "plt.tight_layout()\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "88d49e04",
      "metadata": {
        "id": "88d49e04",
        "outputId": "00eda572-3ef3-452e-e83b-5ba26b3e236a"
      },
      "outputs": [
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "#showing the most common words between the speakers\n",
        "plt.figure(figsize=(10, 8))\n",
        "sns.countplot(data=df_new, y='u', order=df_new['u'].value_counts().head(15).index)\n",
        "plt.xlabel('Count')\n",
        "plt.ylabel('u')\n",
        "plt.title('Top 15 u')\n",
        "plt.tight_layout()\n",
        "plt.show()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "49bc9629",
      "metadata": {
        "id": "49bc9629"
      },
      "source": [
        "# Training a simple classifier"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "27fb28fe",
      "metadata": {
        "id": "27fb28fe"
      },
      "outputs": [],
      "source": [
        "#train_set, test_set = train_test_split(df_new, test_size=0.2)\n",
        "#train_set, test_set"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "86a0a306",
      "metadata": {
        "id": "86a0a306"
      },
      "source": [
        "# Here i would be addding the logistic regression and getting its Validation Accuracy"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "cf05ac34",
      "metadata": {
        "id": "cf05ac34",
        "outputId": "ccdf275e-b459-4e96-cda0-4f9f73761dcc"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Test Accuracy: 0.25742574257425743\n"
          ]
        }
      ],
      "source": [
        "from sklearn.feature_extraction.text import CountVectorizer\n",
        "\n",
        "# Split the dataset into features (X) and target (y)\n",
        "X_text = df_new['u'].values\n",
        "y = df_new['agerange'].values\n",
        "\n",
        "# Split the data into training and testing sets\n",
        "X_train_text, X_test_text, y_train, y_test = train_test_split(X_text, y, test_size=0.2, random_state=8)\n",
        "\n",
        "# Convert text data which is the utterence to numerical representation using CountVectorizer\n",
        "vectorizer = CountVectorizer()\n",
        "X_train = vectorizer.fit_transform(X_train_text)\n",
        "X_test = vectorizer.transform(X_test_text)\n",
        "\n",
        "# Train the logistic regression classifier\n",
        "classifier = LogisticRegression(max_iter=128)\n",
        "classifier.fit(X_train, y_train)\n",
        "y_pred = classifier.predict(X_test)\n",
        "\n",
        "# Evaluate the model's performance\n",
        "accuracy = classifier.score(X_test, y_test)\n",
        "print(\"Test Accuracy:\", accuracy)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "b3cb8d0a",
      "metadata": {
        "id": "b3cb8d0a"
      },
      "source": [
        "# Splitting the data"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "640b37f4",
      "metadata": {
        "id": "640b37f4"
      },
      "source": [
        "# Here Examining errors by calling the precision, recall, f1-score, support"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "24bb974b",
      "metadata": {
        "id": "24bb974b",
        "outputId": "acf1f498-8fb9-4311-ad2d-0564290c05db"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "        0_10       0.00      0.00      0.00        23\n",
            "       11_18       0.07      0.02      0.04        42\n",
            "       19_29       0.32      0.63      0.42       167\n",
            "       30_39       0.20      0.17      0.19        63\n",
            "       40_49       0.24      0.10      0.15        67\n",
            "       50_59       0.11      0.07      0.09        58\n",
            "       60_69       0.03      0.02      0.03        41\n",
            "       70_79       0.00      0.00      0.00        30\n",
            "       80_89       0.00      0.00      0.00         9\n",
            "       90_99       0.00      0.00      0.00         5\n",
            "\n",
            "    accuracy                           0.26       505\n",
            "   macro avg       0.10      0.10      0.09       505\n",
            "weighted avg       0.18      0.26      0.20       505\n",
            "\n"
          ]
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "C:\\Users\\3mabd\\anaconda3\\lib\\site-packages\\sklearn\\metrics\\_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n",
            "C:\\Users\\3mabd\\anaconda3\\lib\\site-packages\\sklearn\\metrics\\_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n",
            "C:\\Users\\3mabd\\anaconda3\\lib\\site-packages\\sklearn\\metrics\\_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n"
          ]
        }
      ],
      "source": [
        "# precision, recall, F1-score, and support\n",
        "classification_metrics = classification_report(y_test, y_pred)\n",
        "print(classification_metrics)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "630ce84f",
      "metadata": {
        "id": "630ce84f",
        "outputId": "094d1949-01e3-43cf-c846-ad39aa23d442"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Precision: 0.09729080741316559\n",
            "Recall: 0.10309766104189708\n",
            "Confusion Matrix:\n",
            " [[  0   0  18   2   1   0   2   0   0   0]\n",
            " [  0   1  33   3   2   1   2   0   0   0]\n",
            " [  1   5 106  20  12   9  14   0   0   0]\n",
            " [  1   1  40  11   0   7   3   0   0   0]\n",
            " [  1   1  43   5   7   3   7   0   0   0]\n",
            " [  1   4  37   7   2   4   2   1   0   0]\n",
            " [  0   0  27   3   4   6   1   0   0   0]\n",
            " [  1   1  21   2   1   4   0   0   0   0]\n",
            " [  0   2   4   2   0   0   0   1   0   0]\n",
            " [  0   0   4   0   0   1   0   0   0   0]]\n"
          ]
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "C:\\Users\\3mabd\\anaconda3\\lib\\site-packages\\sklearn\\metrics\\_classification.py:1318: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n"
          ]
        },
        {
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 576x432 with 2 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          },
          "output_type": "display_data"
        }
      ],
      "source": [
        "# precision, recall, and confusion matrix for the logistic regression\n",
        "precision = precision_score(y_test, y_pred, average='macro')\n",
        "recall = recall_score(y_test, y_pred, average='macro')\n",
        "confusion = confusion_matrix(y_test, y_pred)\n",
        "\n",
        "print(\"Precision:\", precision)\n",
        "print(\"Recall:\", recall)\n",
        "print(\"Confusion Matrix:\\n\", confusion)\n",
        "# Plot the confusion matrix as a heatmap\n",
        "plt.figure(figsize=(8, 6))\n",
        "sns.heatmap(confusion, annot=True, cmap=\"Blues\", fmt=\"d\", xticklabels=classifier.classes_, yticklabels=classifier.classes_)\n",
        "plt.xlabel(\"Predicted Labels\")\n",
        "plt.ylabel(\"True Labels\")\n",
        "plt.title(\"Confusion Matrix\")\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "77facc44",
      "metadata": {
        "id": "77facc44"
      },
      "source": [
        "# Adding the Random forest model"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "586c6855",
      "metadata": {
        "id": "586c6855"
      },
      "outputs": [],
      "source": [
        "from sklearn.ensemble import RandomForestClassifier\n",
        "# Convert text data to numerical representation using CountVectorizer\n",
        "vectorizer = CountVectorizer()\n",
        "X_train = vectorizer.fit_transform(X_train_text)\n",
        "X_val = vectorizer.transform(X_val_text)\n",
        "\n",
        "# Random Forest Classifier being specified\n",
        "complex_model = RandomForestClassifier(n_estimators=100)\n",
        "complex_model.fit(X_train, y_train)\n",
        "# Predictions on the validation set\n",
        "y_val_pred = complex_model.predict(X_val)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "7b53e885",
      "metadata": {
        "id": "7b53e885",
        "outputId": "19499d74-507f-45ce-ae54-6b93b8a59b86"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "C:\\Users\\3mabd\\anaconda3\\lib\\site-packages\\sklearn\\metrics\\_classification.py:1318: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n"
          ]
        }
      ],
      "source": [
        "y_val_pred = np.array(y_val_pred).flatten()\n",
        "y_val = np.array(y_val).flatten()\n",
        "\n",
        "# accuracy, precision, recall, and confusion matrix\n",
        "accuracy = accuracy_score(y_val, y_val_pred)\n",
        "precision = precision_score(y_val, y_val_pred, average='macro')\n",
        "recall = recall_score(y_val, y_val_pred, average='macro')\n",
        "confusion_mat = confusion_matrix(y_val, y_val_pred)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "85b6114e",
      "metadata": {
        "id": "85b6114e"
      },
      "source": [
        "* getting the accuracy score on the validation set\n",
        "* precision, recall, and confusion matrix readings"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8042bb36",
      "metadata": {
        "id": "8042bb36",
        "outputId": "76ddd384-28f3-4dac-c195-f7af3b6fa5d3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Validation Accuracy: 21.78%\n",
            "Validation Precision: 0.10\n",
            "Validation Recall: 0.09\n",
            "Confusion Matrix:\n",
            "[[ 1  2 15  1  1  0  3  0  0  0]\n",
            " [ 0  4 29  4  1  1  2  1  0  0]\n",
            " [ 5 15 90 20 23  8  4  2  0  0]\n",
            " [ 2  4 36  6  6  8  1  0  0  0]\n",
            " [ 1  4 47  4  5  1  5  0  0  0]\n",
            " [ 0  5 36  8  4  3  1  0  1  0]\n",
            " [ 0  5 24  3  5  2  0  1  1  0]\n",
            " [ 0  1 18  5  1  2  2  1  0  0]\n",
            " [ 1  1  4  1  0  1  0  1  0  0]\n",
            " [ 2  0  3  0  0  0  0  0  0  0]]\n",
            "Misclassified Samples:\n",
            "  (0, 854)\t1\n",
            "  (0, 988)\t1\n",
            "  (0, 1264)\t1\n",
            "  (1, 621)\t1\n",
            "  (1, 1284)\t1\n",
            "  (2, 1453)\t1\n",
            "  (3, 192)\t1\n",
            "  (4, 214)\t1\n",
            "  (4, 395)\t1\n",
            "  (4, 823)\t1\n",
            "  (5, 39)\t2\n",
            "  (5, 270)\t1\n",
            "  (5, 368)\t1\n",
            "  (5, 1207)\t1\n",
            "  (6, 7)\t1\n",
            "  (6, 56)\t1\n",
            "  (6, 586)\t1\n",
            "  (6, 831)\t1\n",
            "  (6, 849)\t1\n",
            "  (6, 1278)\t1\n",
            "  (6, 1410)\t1\n",
            "  (7, 1453)\t1\n",
            "  (8, 551)\t1\n",
            "  (8, 719)\t1\n",
            "  (8, 1007)\t1\n",
            "  :\t:\n",
            "  (392, 849)\t1\n",
            "  (392, 1101)\t1\n",
            "  (392, 1102)\t1\n",
            "  (392, 1299)\t2\n",
            "  (392, 1352)\t1\n",
            "  (392, 1360)\t1\n",
            "  (392, 1398)\t1\n",
            "  (392, 1402)\t1\n",
            "  (393, 46)\t1\n",
            "  (393, 468)\t1\n",
            "  (393, 510)\t1\n",
            "  (393, 516)\t1\n",
            "  (393, 692)\t1\n",
            "  (393, 775)\t1\n",
            "  (393, 861)\t1\n",
            "  (393, 1028)\t1\n",
            "  (393, 1284)\t1\n",
            "  (393, 1445)\t1\n",
            "  (394, 129)\t1\n",
            "  (394, 328)\t1\n",
            "  (394, 621)\t1\n",
            "  (394, 692)\t1\n",
            "  (394, 849)\t1\n",
            "  (394, 1097)\t1\n",
            "  (394, 1264)\t1\n",
            "Misclassified Labels:\n",
            "['30_39' '60_69' '40_49' '50_59' '60_69' '70_79' '19_29' '50_59' '19_29'\n",
            " '19_29' '70_79' '11_18' '50_59' '11_18' '30_39' '70_79' '50_59' '60_69'\n",
            " '30_39' '80_89' '60_69' '40_49' '30_39' '40_49' '40_49' '19_29' '19_29'\n",
            " '50_59' '60_69' '40_49' '19_29' '70_79' '11_18' '50_59' '11_18' '40_49'\n",
            " '60_69' '50_59' '19_29' '19_29' '30_39' '11_18' '11_18' '50_59' '19_29'\n",
            " '30_39' '60_69' '90_99' '11_18' '40_49' '0_10' '30_39' '40_49' '60_69'\n",
            " '19_29' '60_69' '50_59' '50_59' '11_18' '80_89' '40_49' '80_89' '19_29'\n",
            " '19_29' '0_10' '40_49' '30_39' '70_79' '70_79' '30_39' '40_49' '90_99'\n",
            " '30_39' '30_39' '60_69' '40_49' '0_10' '30_39' '0_10' '40_49' '60_69'\n",
            " '19_29' '40_49' '50_59' '11_18' '80_89' '30_39' '0_10' '40_49' '40_49'\n",
            " '19_29' '50_59' '0_10' '60_69' '40_49' '80_89' '40_49' '19_29' '30_39'\n",
            " '11_18' '40_49' '40_49' '11_18' '19_29' '40_49' '50_59' '70_79' '19_29'\n",
            " '11_18' '40_49' '19_29' '30_39' '19_29' '50_59' '40_49' '19_29' '30_39'\n",
            " '19_29' '70_79' '40_49' '11_18' '19_29' '30_39' '40_49' '40_49' '30_39'\n",
            " '40_49' '19_29' '50_59' '70_79' '30_39' '40_49' '11_18' '40_49' '70_79'\n",
            " '70_79' '19_29' '19_29' '60_69' '50_59' '0_10' '70_79' '40_49' '19_29'\n",
            " '60_69' '11_18' '19_29' '19_29' '11_18' '19_29' '70_79' '11_18' '19_29'\n",
            " '60_69' '0_10' '50_59' '0_10' '60_69' '60_69' '50_59' '80_89' '40_49'\n",
            " '50_59' '30_39' '50_59' '50_59' '0_10' '60_69' '40_49' '50_59' '90_99'\n",
            " '19_29' '40_49' '40_49' '50_59' '30_39' '50_59' '60_69' '70_79' '60_69'\n",
            " '11_18' '30_39' '30_39' '40_49' '19_29' '40_49' '40_49' '30_39' '50_59'\n",
            " '19_29' '50_59' '19_29' '70_79' '0_10' '50_59' '19_29' '40_49' '19_29'\n",
            " '40_49' '70_79' '50_59' '19_29' '60_69' '50_59' '30_39' '0_10' '19_29'\n",
            " '70_79' '50_59' '40_49' '50_59' '50_59' '19_29' '50_59' '30_39' '11_18'\n",
            " '50_59' '60_69' '19_29' '40_49' '50_59' '50_59' '40_49' '11_18' '0_10'\n",
            " '19_29' '60_69' '30_39' '90_99' '70_79' '11_18' '30_39' '30_39' '30_39'\n",
            " '50_59' '40_49' '70_79' '60_69' '19_29' '11_18' '0_10' '0_10' '19_29'\n",
            " '30_39' '19_29' '60_69' '40_49' '30_39' '50_59' '11_18' '30_39' '60_69'\n",
            " '11_18' '19_29' '19_29' '90_99' '50_59' '30_39' '30_39' '19_29' '40_49'\n",
            " '60_69' '19_29' '19_29' '70_79' '60_69' '50_59' '11_18' '30_39' '40_49'\n",
            " '19_29' '60_69' '30_39' '50_59' '70_79' '60_69' '19_29' '0_10' '19_29'\n",
            " '30_39' '11_18' '50_59' '60_69' '11_18' '40_49' '19_29' '60_69' '30_39'\n",
            " '70_79' '19_29' '30_39' '19_29' '19_29' '80_89' '50_59' '19_29' '19_29'\n",
            " '70_79' '30_39' '19_29' '70_79' '30_39' '0_10' '60_69' '60_69' '30_39'\n",
            " '50_59' '0_10' '30_39' '50_59' '19_29' '11_18' '19_29' '40_49' '19_29'\n",
            " '50_59' '11_18' '19_29' '19_29' '60_69' '80_89' '11_18' '60_69' '30_39'\n",
            " '11_18' '60_69' '0_10' '70_79' '19_29' '40_49' '60_69' '30_39' '40_49'\n",
            " '40_49' '19_29' '70_79' '19_29' '30_39' '50_59' '0_10' '40_49' '11_18'\n",
            " '11_18' '19_29' '19_29' '19_29' '30_39' '50_59' '60_69' '40_49' '0_10'\n",
            " '19_29' '30_39' '40_49' '50_59' '50_59' '30_39' '19_29' '40_49' '30_39'\n",
            " '11_18' '30_39' '50_59' '19_29' '70_79' '50_59' '30_39' '30_39' '11_18'\n",
            " '50_59' '30_39' '19_29' '0_10' '40_49' '70_79' '19_29' '40_49' '50_59'\n",
            " '11_18' '11_18' '30_39' '60_69' '19_29' '80_89' '19_29' '60_69' '40_49'\n",
            " '40_49' '30_39' '50_59' '40_49' '40_49' '70_79' '40_49' '11_18']\n"
          ]
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "C:\\Users\\3mabd\\anaconda3\\lib\\site-packages\\sklearn\\metrics\\_classification.py:1318: UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
            "  _warn_prf(average, modifier, msg_start, len(result))\n"
          ]
        }
      ],
      "source": [
        "# Calculate the validation accuracy\n",
        "accuracy = accuracy_score(y_val, y_val_pred)\n",
        "print(\"Validation Accuracy: {:.2f}%\".format(accuracy * 100))\n",
        "# Calculate the validation precision and validation recall\n",
        "precision = precision_score(y_val, y_val_pred, average='macro')\n",
        "print(\"Validation Precision: {:.2f}\".format(precision))\n",
        "recall = recall_score(y_val, y_val_pred, average='macro')\n",
        "print(\"Validation Recall: {:.2f}\".format(recall))\n",
        "\n",
        "# Calculate the confusion matrix\n",
        "confusion_mat = confusion_matrix(y_val, y_val_pred)\n",
        "print(\"Confusion Matrix:\")\n",
        "print(confusion_mat)\n",
        "\n",
        "\n",
        "# Error analysis\n",
        "misclassified_samples = X_val[y_val != y_val_pred]\n",
        "misclassified_labels = y_val[y_val != y_val_pred]\n",
        "print(\"Misclassified Samples:\")\n",
        "print(misclassified_samples)\n",
        "print(\"Misclassified Labels:\")\n",
        "print(misclassified_labels)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "bd4f06a8",
      "metadata": {
        "id": "bd4f06a8"
      },
      "source": [
        "# Comparing the accuracies in a table"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "8ca0d60a",
      "metadata": {
        "id": "8ca0d60a",
        "outputId": "891c3c00-280c-4fa4-98a3-c7e694976aa0"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "                        Model  Accuracy\n",
            "0  Simple Logistic Regression  0.217822\n",
            "1       Complex Random Forest  0.217822\n"
          ]
        }
      ],
      "source": [
        "# adding the accurcy for the logistic regression\n",
        "simple_accuracy = accuracy\n",
        "\n",
        "# Calculating the accuracy for the Complex Random Forest Classifier\n",
        "complex_accuracy = complex_model.score(X_val, y_val)\n",
        "# Create a DataFrame to store the accuracies\n",
        "accuracies_df = pd.DataFrame({\n",
        "                              'Model': ['Simple Logistic Regression', 'Complex Random Forest'],\n",
        "                               'Accuracy': [simple_accuracy, complex_accuracy]\n",
        "})\n",
        "print(accuracies_df)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f11fce54",
      "metadata": {
        "id": "f11fce54"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.12"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}
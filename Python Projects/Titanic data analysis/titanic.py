import pandas as pd
import matplotlib.pyplot as plt


def main():
	filepath = 'titanic_data/train.csv'
	data = pd.read_csv(filepath)
	print(data)
	print(data.count())

	plt.figure(figsize=(18,7))
	########################
	plt.subplot2grid((3, 4),(0, 0))
	data.Survived.value_counts(normalize=True).sort_index().plot(kind='bar', color='red')
	plt.title('Survived')

	plt.subplot2grid((3, 4), (0, 1))
	data.Pclass.value_counts(normalize=True).sort_index().plot(kind='bar', color='yellow')
	plt.title('Pclass')

	plt.subplot2grid((3, 4), (0, 2))
	data.Sex.value_counts(normalize=True).sort_index().plot(kind='bar', color='green')
	plt.title('Sex')

	plt.subplot2grid((3, 4), (0, 3))
	data.Age.value_counts(normalize=True).sort_index().plot(kind='bar', color='purple')
	plt.title('Age')

	plt.subplot2grid((3, 4), (1, 0))
	data.Survived[data.Sex == 'male'].value_counts(normalize=True).sort_index().plot(kind='bar', color='blue')
	plt.title('Survived_male')

	plt.subplot2grid((3, 4), (1, 1))
	data.Survived[data.Fare == 71.2833].value_counts(normalize=True).sort_index().plot(kind='bar', color='grey')
	plt.title('Survived_fare')

	plt.subplot2grid((3, 4), (2, 0))
	data.Survived[data.Sex == 'male'][data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar', color='green')
	plt.title('rich men survived')

	plt.subplot2grid((3, 4), (2, 1))
	data.Survived[data.Sex == 'male'][data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar',
																								   color='green')
	plt.title('poor men survived')

	plt.subplot2grid((3, 4), (2, 2))
	data.Survived[data.Sex == 'female'][data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar',
																									   color='red')
	plt.title('rich women survived')

	plt.subplot2grid((3, 4), (2, 3))
	data.Survived[data.Sex == 'female'][data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar',
																										 color='red')
	plt.title('poor women survived')

	########################
	plt.show()


if __name__ == '__main__':
	main()

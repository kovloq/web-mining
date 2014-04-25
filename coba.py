f=open("../Documents/NLP/TripAdvisor/tagged_hotels_corpus.txt");
raw=f.read();
baris=raw.split("\n");
for bar in baris:
	print bar;
f.close();
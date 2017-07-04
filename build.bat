call buildres.bat;
pyinstaller --clean --onefile --noconsole --distpath ./dist --workpath ./build -i ./res/icon.ico ./src/main.py
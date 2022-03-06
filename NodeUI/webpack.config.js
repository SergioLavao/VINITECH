const path = require('path');

module.exports = 
{
	watch: true,
	mode: "development",
	entry: "./src/index.js",
	output:
	{

		path: path.resolve( __dirname , "../main/static/" ),
		filename: "build.js"

	}
}
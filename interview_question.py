"""
Example

Input:
file_paths = [
	"youtube/videos/2024/movie.mp4",
	"youtube/videos/2023/documentary.mp4",
	"youtube/music/2024/song.mp3",
	"documents/work/report.docx",
	"documents/personal/tax.pdf"
	"documents/personal/book.pdf"
]

Output:
tree = {
	"youtube": {
		"videos": {
			"2024": [
				"movie.mp4"
			],
			"2023": [
				"documentary.mp4"
			]
		},
		"music": {
			"2024": [
				"song.mp3"
			]
		}
	},
	"documents": {
		"work": [
			"report.docx"
		],
		"personal": [
			"tax.pdf",
			"book.pdf"
		]
	}
}
"""

import json

file_paths = [
	"media/movies/2023/action/blockbuster.mkv",
	"media/movies/2023/comedy/funny_movie.mp4",
	"media/movies/2024/drama/dramatic_film.avi",
	"media/tv_shows/season1/episode1.mkv",
	"media/tv_shows/season1/episode2.mkv",
	"media/tv_shows/season2/episode1.mkv",
	"documents/reports/2021/annual_report.pdf",
	"documents/reports/2022/financial_report.pdf",
	"documents/reports/2023/marketing_report.docx",
	"documents/personal/letters/cover_letter.docx",
	"downloads/ebooks/programming/python_guide.pdf",
	"downloads/ebooks/science/space_exploration.pdf",
	"archive/music/2020/rock_album/song.mp3",
	"archive/music/2019/pop_album/song.mp3",
	"archive/movies/old_movie.mp4"
]

def create_tree_structure(paths: list[str]) -> dict:
	"""
	Args:
		paths: list of file paths
	Returns: 
		A dictionary representing the tree structure of the file paths
	"""
	pass

def test(tree: dict) -> None:
	print(json.dumps(tree, indent = 4))

test(create_tree_structure(file_paths))
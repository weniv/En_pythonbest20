# PAGE_NAME으로 바로 호출 가능하도록 0번째 값을 비워줌
testcase_and_result = [{
    "que_number": 0,
    "lv" : "",
    "kinds": "",
    "testcase": "",
    "result": ""
}, {
    "que_number": 1,
    "lv" : 0,
    "kinds": "Implementation",
    "testcase": [["  + + - + -+-", "  ++--+-+  ", "++ -+ -+-", "+++- +-+"], ["++-- -++", "++-- --+", "+++- +--"], ["++-++--", "++-+--+", "++-++++", "++-+++-"]],
    "result": ["jeju", "cat", "lion"]
}, {
    "que_number": 2,
    "lv" : 1,
    "kinds": "Regular Expression",
    "testcase": ["adr10bb1d9ia10e33b7u88k3j1a3v11v9", "r1rr2rrr3rrrrr4rrrrrre5", "12345r12345e90v90r90"],
    "result": ["Feb 3", "Jan 5", "Feb 8"]
}, {
    "que_number": 3,
    "lv" : 1,
    "kinds": "Sorting",
    "testcase": [
        [["A", 25, 24, 11, 12], ["B", 13, 22, 16, 14], ["C", 12, 22, 16, 14], ["D", 13, 22, 16, 14], ["E", 12, 25, 16, 19], [
            "F", 23, 15, 16, 14], ["G", 13, 14, 3, 5], ["H", 25, 22, 11, 14], ["I", 13, 12, 14, 23], ["J", 13, 22, 15, 14]],
        [["A", 11, 23, 17, 15], ["B", 15, 22, 17, 22], ["C", 13, 22, 16, 14],
            ["D", 18, 22, 16, 25], ["E", 8, 13, 23, 21]],
        [["A", 25, 25, 25, 25], ["B", 25, 25, 25, 25], [
            "C", 25, 25, 25, 25], ["J", 13, 22, 16, 14]]
    ],
    "result": [["H", "E", "A"], ["D"], []]
}, {
    "que_number": 4,
    "lv" : 1,
    "kinds": "Regular Expression",
    "testcase": [
        ["10 - \"A\". 20 - \"B\". 30 - \"A\".", "1 - \"A\". 1 - \"A\". 1 - \"A\". 1 - \"A\". 2 - \"B\". 1 - \"A\". 1 - \"B\"."],
        ["10 \"a\". 10 \"a\". 10 \"a\". 20 \"b\". 30 \"c\".", "\"c\" -- 100. \"c\" -- 100. \"c\" -- 100."],
        ["Practiced \"A\" as much as 100. Practiced \"B\" as much as 200. Practiced \"C\" as much as 300.", "Practiced \"D\" as much as 100. Practiced \"E\" as much as 200"]
    ],
    "result": [
    "The final design of the dream was originally 260 but changed to 14760. We create Vision based on these numbers.",
    "The final design of the dream was originally 9000 but changed to 52000. We create Vision based on these numbers.",
    "The future is not visible."]
}, {
    "que_number": 5,
    "lv" : 1,
    "kinds": "Matrix",
    "testcase": [
        [[0, "#"], [0, 0]],
        [[0, 0, "#", "#"], ["#", "#", 0, "#"], [0, "#", "#", 0]],
        [["#", 0, 0, 0, "#"], [0, "#", "#", 0, 0], ["#", "#", "#", 0, "#"], ["#", 0, 0, "#", "#"]]    
    ],
    "result": [[1, 3], [7, 16], [11, 29]]
}, {
    "que_number": 6,
    "lv" : 1,
    "kinds": "Stack, Queue",
    "testcase": [
        [1, 2, 3, 4, 1, 1, 2, 3, 4],
        [1, 1, 1, 2, 3, 4, 2, 3, 4, 1],
        [1, 2, 3, 4, 2, 3, 4, 1]
    ],
    "result": [1, 2, 0]
}, {
    "que_number": 7,
    "lv" : 1,
    "kinds": "Two Pointers, Sliding Window",
    "testcase": [
        [[4, 9, 11, 2], 6],
        [[2, 2], 4],
        [[1, 5, 10, 20, 93], 103]
    ],
    "result": [
        [0, 3],
        [0, 1],
        [2, 4]
    ]
}, {
    "que_number": 8,
    "lv" : 0,
    "kinds": "Math",
    "testcase": [100, 36000, 66600],
    "result": [0, 12, 22]
}, {
    "que_number": 9,
    "lv" : 1,
    "kinds": "Two Pointers, Sliding Window",
    "testcase": [[58000, 58700, 55300, 54200, 53600, 52700, 57700, 61100], [80000, 58000, 52700, 57700, 61100], [100, 2000, 30000, 400000]],
    "result": [6000, 27300, 0]
}, {
    "que_number": 10,
    "lv" : 1,
    "kinds": "Combination",
    "testcase": [[0, ""], [2, "salmon"], [3, ""]],
    "result": ["Basic Poke will be provided.", [["salmon", "tuna"], ["salmon", "chicken"], ["salmon", "bacon"], ["salmon", "mushroom"]],
               [["salmon", "tuna", "chicken"], ["salmon", "tuna", "bacon"], ["salmon", "tuna", "mushroom"], ["salmon", "chicken", "bacon"], ["salmon", "chicken", "mushroom"], ["salmon", "bacon", "mushroom"], ["tuna", "chicken", "bacon"], ["tuna", "chicken", "mushroom"], ["chicken", "bacon", "mushroom"]]
               ]
}, {
    "que_number": 11,
    "lv" : 3,
    "kinds": "Tree, LinkedList, Trie",
    "testcase": [
        ["sky", "ground", "sea"],
        ["one-two", "two-three", "three-four", "one-five", "six-seven"],
        ["jeju-coding-basecamp", "coding-camp"]
    ],
    "result": [
        "sky\n\nground\n\nsea\n\n",
        "six\n  └ seven\n\none\n  ├ five\n  └ two\n      └ three\n          └ four",
        "jeju\n  └ coding\n      ├ camp\n      └ basecamp"
    ]
}, {
    "que_number": 12,
    "lv" : 3,
    "kinds": "Permutations, Brute-force",
    "testcase": [
        [2, 4, 1, 3, 5, 8, 8, 6],
        [10, 2, 5, 2, 7, 9, 3, 5],
        [12, 9, 7, 8, 6, 2, 2, 6]
    ],
    "result": [21, 29, 31]
}, {
    "que_number": 13,
    "lv" : 1,
    "kinds": "Heap",
    "testcase": [[[46, 26, 37, 32, 10], 30], [[22, 45, 1, 7, 5], 15], [[7, 36, 25, 12, 22], 47]],
    "result": [4, 2, 2]
}, {
    "que_number": 14,
    "lv" : 1,
    "kinds": "DFS/BFS",
    "testcase": [[[1, 3, "#"], [0, "#", 2], [0, 1, 1]], [[0, "#", 1, 0], [2, 1, 1, 2], ["#", 3, 0, 1], [1, "#", "#", 3], [0, 2, "#", 1]], [[1, "#", 1], [2, 1, "#"], ["#", "#", 0], [1, "#", 1]]],
    "result": [8, 15, -1]
}, {
    "que_number": 15,
    "lv" : 2,
    "kinds": "matrix",
    "testcase": [
        [5, 5, 3, [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]],
        [7, 5, 4, [[0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]],
        [4, 3, 2, [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]]
    ],
    "result": [7, 2, 5]
}, {
    "que_number": 16,
    "lv" : 1,
    "kinds": "Implementation",
    "testcase": [[73, 88, 86], [67, 86, 77, 76], [68, 86, 76, 73, 88]],
    "result": [16, 1155, 566]
}, {
    "que_number": 17,
    "lv" : 1,
    "kinds": "binary tree",
    "testcase": [
        [[2, 4, 1, 7, 9, 8, 12],[2, 4, 8, 3, 6]],
        [[3, 6, 9, 1, 8, 7], [3, 8]],
        [[102, 21, 38, 52, 219, 63, 1, 9, 35], [36, 9, 95, 32, 7, 52, 102]]
    ],
    "result": [[3, 6], [], [7, 32, 36, 95]]
}, {
    "que_number": 18,
    "lv" : 1,
    "kinds": "Implementation",
    "testcase": [
        [["Korean Shorthair", "Korean Shorthair", "Maine Coon", "Bengal", "Maine Coon", "British Shorthair", "Norwegian Forest" ], [30, 15, 13, 4, 45, 9, 21]], 
        [["Sphynx", "British Shorthair", "Sphynx", "Sphynx", "Bengal", "Maine Coon"], [3, 16, 1, 9, 25, 5]], 
        [["Maine Coon", "Korean Shorthair", "British Shorthair", "Norwegian Forest", "Norwegian Forest", "Korean Shorthair", "Korean Shorthair"], [8, 32, 15, 17, 12, 13, 31]]
    ],
    "result": [["Maine Coon", "Korean Shorthair",  "Norwegian Forest", "British Shorthair", "Bengal"], ["Bengal", "British Shorthair", "Sphynx", "Maine Coon"], ["Korean Shorthair", "Norwegian Forest", "British Shorthair", "Maine Coon"]]

}, {
    "que_number": 19,
    "lv" : 1,
    "kinds": "Greedy",
    "testcase": [[[45, 5, 3, 15],100], [[6, 2, 4, 8, 32], 50], [[7, 2, 14, 28], 74]],
    "result": [4, 4, 5]
}, {
    "que_number": 20,
    "lv" : 2,
    "kinds": "sorting",
    "testcase": [
        [[["strawberry", "cream", "flour", "butter"], [15, 8, 4, 20], [4, 3, 2, 1]], 40], 
		[[["milk", "egg", "butter", "chocolate cinnamon", "pineapple", "cream"], [10, 5, 5, 18, 6, 3], [1, 3, 2, 4, 5, 6]], 10], 
		[[["strawberry", "milk", "butter", "chocolate cinnamon", "green grape", "cream"], [120, 150, 130, 118, 126, 130], [6, 5, 4, 3, 2, 1]], 100]
    ],
    "result": [
        ["butter", "flour", "cream"],
		["milk"],
		[]
    ]
}]

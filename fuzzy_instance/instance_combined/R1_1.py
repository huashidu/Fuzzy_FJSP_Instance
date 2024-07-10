# instance1 5*4

machine_num = [4]

processing_factory = [
    [  # Factory1
        [  # Job1
            [1, 2],
            [1, 4],
            [1],
            [2]
        ],
        [  # Job2
            [1, 4],
            [3, 4],
            [1, 3],
            [1, 2]
        ],
        [  # Job3
            [2, 3],
            [2, 3, 4],
            [1, 2, 4],
            [2, 3]
        ],
        [  # Job4
            [1, 2],
            [2, 4],
            [3, 4],
            [1, 2, 4]
        ],
        [  # Job5
            [1, 2, 3, 4],
            [4],
            [2, 3, 4],
            [1, 2, 3, 4]
        ]
    ]
]

fuzzy_processing_time = [
    [  # Factory1
        [  # Job1
            [  # Operator1
                [5, 8, 11],
                [4, 7, 9]
            ],
            [  # Operator2
                [6, 9, 12],
                [3, 5, 8]
            ],
            [  # Operator3
                [9, 11, 14]
            ],
            [  # Operator4
                [9, 12, 15]
            ]
        ],
        [  # Job2
            [  # Operator1
                [10, 14, 17],
                [5, 6, 9]
            ],
            [  # Operator2
                [6, 9, 10]
            ],
            [  # Operator3
                [5, 8, 9],
                [6, 8, 11]
            ],
            [  # Operator4
                [7, 8, 10],
                [9, 11, 14]
            ]
        ],
        [  # Job3
            [  # Operator1
                [4, 5, 6],
                [2, 3, 6]
            ],
            [  # Operator2
                [7, 9, 12],
                [6, 9, 11],
                [7, 8, 11]
            ],
            [  # Operator3
                [10, 14, 17],
                [5, 7, 10]
            ],
            [  # Operator4
                [3, 5, 9],
                [5, 9, 12]
            ]
        ],
        [  # Job4
            [  # Operator1
                [3, 5, 6],
                [4, 7, 10]
            ],
            [  # Operator2
                [4, 7, 8],
                [5, 8, 10]
            ],
            [  # Operator3
                [4, 5, 7],
                [5, 8, 10]
            ],
            [  # Operator4
                [5, 8, 11],
                [9, 12, 14],
                [6, 9, 12]
            ]
        ],
        [  # Job5
            [  # Operator1
                [3, 6, 8],
                [4, 5, 7],
                [8, 9, 11],
                [7, 10, 14]
            ],
            [  # Operator2
                [3, 5, 8]
            ],
            [  # Operator3
                [7, 10, 12],
                [6, 7, 8],
                [5, 8, 12]
            ],
            [  # Operator4
                [8, 10, 13],
                [7, 9, 12],
                [8, 10, 12],
                [6, 9, 12]
            ]
        ]
    ]
]

# Note
* Chạy trên hệ điều hành Windows
* Trước khi chạy phải active môi trường virtualenv
* Chạy lệnh ```pip install -r requirements.txt``` để cài các package cần thiết
* **Challenge 6** elasticSearch chạy trên cổng 9200
* Chạy **Challenge 5** để insert dữ liệu vào elasticSearch
## Challenge 1,2,3,5,6
* Chạy như bình thường, chỉ chạy file \*.py trong thư mục là được 
## Challenge 4
* Chạy file **runner.py** trong thư mục CodeChanllgesP3
* Dữ liệu crawl được sẽ nằm trong file **science.json** trong cùng thư mục với file **runner.py**
# API của Challenge 6
* ## Insert
> [http://localhost:8000/insert](http://http://localhost:8000/insert)
`Method Post`
* **body**
> {
            "title": "title",
            "content": "content",
            "published_date": "published_date"
        }
* ## Update
> [http://localhost:8000/update](http://http://localhost:8000/update)
`Method Put`
* **body**
> {
            "title": "title",
            "content": "content",
            "published_date": "published_date"
            "ids":"dsdsds"
        }
* ## Delete one
> [http://localhost:8000/delete_one/\<ids>](http://http://localhost:8000/delete_one/<ids>)
`Method Delete`

* ## Delete many
> [http://localhost:8000/delete_many](http://http://localhost:8000/delete_many)
`Method Post`
* **body**
> {"ids": ["sdsd","2434"]}

* ## get by id one
> [http://localhost:8000/get_by_id_one/\<ids>](http://http://localhost:8000/get_by_id_one/<ids>)
`Method Get`
 
* ## Get by id many
> [http://localhost:8000/get_by_id_many](http://http://localhost:8000/get_by_id_many)
`Method Post`
* **body**
> {"ids": ["sdsd","2434"]}

* ## search any
> [http://localhost:8000/search?q=nam](http://http://localhost:8000/search?q=nam)
`Method Get`

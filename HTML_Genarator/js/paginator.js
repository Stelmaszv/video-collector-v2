class Paginator{
    constructor(data,limit){
        this.data=data
        this.limit=limit
    }

    count_pages(){
        return Math.ceil(this.data.length/this.limit)
    }

    genrate_pages(){
        let count = this.data.length
        let pages = this.count_pages()
        let new_array = []
        let index = 0
        for (let i = 0; i < pages; i++){
            movies = []
            let elments = 0
            for (let item of this.data){
                if (elments < this.limit && index < count){
                    movies.push(this.data[index])
                    index = index + 1
                }
                elments = elments + 1
            }
            new_array.push({"page": i, "Objets": movies})
        }
        return new_array
    }
    
}
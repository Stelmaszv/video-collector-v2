from __future__ import annotations
from abc import ABC
from app.db.models import Movies,Series,Stars,Tags,Producent
from app.db.models import session
from sqlalchemy import desc,func
from datetime import date

class AbstractFactory(ABC):

    model=None

    def __init__(self,Menu):
        self.Menu=Menu

    def add_tags(self,query):
        if len(self.Menu.AdvandeSearchCriteria.tags):
            query = query.filter(self.model.tags.any(Tags.name.in_(self.Menu.AdvandeSearchCriteria.tags)))
        return query

    def add_stars(self,query):
        if len(self.Menu.AdvandeSearchCriteria.stars):
            query = query.filter(self.model.stars.any(Stars.name.in_(self.Menu.AdvandeSearchCriteria.stars)))
        return query

    def add_favourite(self,query):
        if self.Menu.AdvandeSearchCriteria.favourite is not None:
            query=query.filter(self.model.favourite == self.Menu.AdvandeSearchCriteria.favourite)
        return query

    def set_query(self):
        if self.Menu.search_faze:
            return session.query(self.model).filter(self.model.name.like(str(self.Menu.search_faze) + '%'))
        return session.query(self.model)

    def add_year(self,query):
        if self.Menu.AdvandeSearchCriteria.year:
            query=query.filter(self.model.AdvandeSearchCriteria.year == self.Menu.AdvandeSearchCriteriayear)
        return query

    def add_min(self,query):
        if self.Menu.AdvandeSearchCriteria.min:
            var=getattr(self.model,self.Menu.AdvandeSearchCriteria.min[0])
            query = query.filter(var >= self.Menu.AdvandeSearchCriteria.min[1])
        return query

    def add_max(self,query):
        if self.Menu.AdvandeSearchCriteria.max and self.Menu.AdvandeSearchCriteria.max[1]>0:
            var=getattr(self.model,self.Menu.AdvandeSearchCriteria.max[0])
            query = query.filter(var <= self.Menu.AdvandeSearchCriteria.max[1])
        return query

    def add_series(self,query):
        if self.Menu.AdvandeSearchCriteria.series:
            query = query.filter(self.model.series.any(Series.name.in_(self.Menu.AdvandeSearchCriteria.series)))
        return query

    def order_by(self,query):
        if self.Menu.AdvandeSearchCriteria.order_by:
            query=query.order_by(desc(self.Menu.AdvandeSearchCriteria.order_by))
        return query

    def return_all(self) -> session:
        query = self.set_query()
        query=self.add_tags(query)
        query=self.add_stars(query)
        query=self.add_favourite(query)
        query=self.add_year(query)
        query=self.add_min(query)
        query = self.add_max(query)
        query =self.add_series(query)
        query = self.order_by(query)
        return query.all()

    def search_faze_normal(self):
        return session.query(self.model).filter(self.model.name.like(str(self.Menu.search_faze) + '%'))

class SetFactory:

    def __init__(self,obj):
        self.obj=obj

    def get_factory(self,name):
        switcher = {
            'movies'     : GetMovies,
            'series'     : GetSeries,
            'stars'      : GetStar,
            'producents' : GetProducents
        }
        classObj = switcher.get(name, "Invalid data");
        return classObj(self.obj).return_all()

class GetProducents(AbstractFactory):

    model = Producent

class GetMovies(AbstractFactory):

    model=Movies

class GetSeries(AbstractFactory):

    model=Series

class GetStar(AbstractFactory):

    model=Stars

    def order_by(self,query):
        if self.Menu.AdvandeSearchCriteria.order_by:
            if self.Menu.AdvandeSearchCriteria.order_by == 'year':
                query= query.filter(
                    func.DATE(self.model.date_of_birth) <
                    date.today()).order_by('date_of_birth')
            else:
                query=query.order_by(desc(self.Menu.AdvandeSearchCriteria.order_by))
        return query

    def return_all(self) -> session:
        query = self.set_query()
        query = self.add_tags(query)
        query = self.add_favourite(query)
        query = self.add_year(query)
        query = self.add_min(query)
        query = self.add_max(query)
        query = self.add_series(query)
        query = self.order_by(query)

        return query.all()






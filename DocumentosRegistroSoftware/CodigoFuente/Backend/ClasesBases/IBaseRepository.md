```
//REPOSITORY IBASEREPOSITORY

package com.persona.Backend.IRepository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.NoRepositoryBean;

@NoRepositoryBean
public interface IBaseRepository<T,ID> extends JpaRepository<T, ID>  {

	List<T> findByDeletedAtIsNullAndStateTrue();
	
	List<T> findByDeletedAtIsNull();
	
}

```
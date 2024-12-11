```
//ENTIDAD ROLE

package com.persona.Backend.Entity.Security;

import com.persona.Backend.Entity.BaseEntity;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "role")
public class Role extends BaseEntity {

	@Column(name = "nombre", length = 45, nullable = false, unique = true)
	private String nombre;

	@Column(name = "descripcion", length = 45, nullable = false)
	private String descripcion;

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

}
//IREPOSITORY ROLE
package com.persona.Backend.IRepository.Security;

import java.util.Optional;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Security.Role;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IRoleRepository extends IBaseRepository<Role, Long>{

	Optional<Role> findByNombre(String nombre);
}
// ISERVICE ROLE

package com.persona.Backend.IService.Security;

import com.persona.Backend.Entity.Security.Role;
import com.persona.Backend.IService.IBaseService;

public interface IRoleService extends IBaseService<Role>{

	Role findByNombre(String nombre);
	
}
// SERVICE ROLE 

package com.persona.Backend.Service.Security;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Security.Role;
import com.persona.Backend.IRepository.Security.IRoleRepository;
import com.persona.Backend.IService.Security.IRoleService;
import com.persona.Backend.Service.BaseService;

@Service
public class RoleService extends BaseService<Role> implements IRoleService{
	
	 @Autowired
	 private IRoleRepository roleRepository;

	@Override
	public Role findByNombre(String nombre) {
		return roleRepository.findByNombre(nombre).orElse(null);
	}

}
//CONTROLLER ROLE

package com.persona.Backend.Controller.Security;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Security.Role;

@CrossOrigin("*")//permite que cualquier dominio tenga acceso a el
@RestController
@RequestMapping("/api/v1/base/security/role")

public class RoleController extends BaseController<Role>{

}

```


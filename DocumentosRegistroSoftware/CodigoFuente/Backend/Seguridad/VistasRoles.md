```
//ENTITY VISTASROLES
package com.persona.Backend.Entity.Security;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "vistas_roles")
public class VistasRoles extends BaseEntity {

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "vista_id", nullable = false, unique = false)
	private Vista vistaId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "role_id", nullable = false, unique = false)
	private Role roleId;

	public Vista getVistaId() {
		return vistaId;
	}

	public void setVistaId(Vista vistaId) {
		this.vistaId = vistaId;
	}

	public Role getRoleId() {
		return roleId;
	}

	public void setRoleId(Role roleId) {
		this.roleId = roleId;
	}

}
//IREPOSITORY VISTASROLES
package com.persona.Backend.IRepository.Security;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Security.VistasRoles;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IVistasRolesRepository extends IBaseRepository<VistasRoles, Long>{

}
//ISERVICE VISTASROLES
package com.persona.Backend.IService.Security;

import com.persona.Backend.Entity.Security.VistasRoles;
import com.persona.Backend.IService.IBaseService;

public interface IVistasRolesService extends IBaseService<VistasRoles>{

}
//SERVICE VISTASROLES
package com.persona.Backend.Service.Security;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Security.VistasRoles;
import com.persona.Backend.IService.Security.IVistasRolesService;
import com.persona.Backend.Service.BaseService;

@Service
public class VistasRolesService extends BaseService<VistasRoles> implements IVistasRolesService{

}
//CONTROLLER VISTASROLES
package com.persona.Backend.Controller.Security;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Security.VistasRoles;

@CrossOrigin("*")//permite que cualquier dominio tenga acceso a el
@RestController
@RequestMapping("/api/v1/base/security/vistas_roles")
public class VistasRolesController extends BaseController<VistasRoles>{

}

```
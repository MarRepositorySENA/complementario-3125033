```
//ENTITY  USUARIOSROLES

package com.persona.Backend.Entity.Security;


import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "usuarios_roles")
public class UsuariosRoles extends BaseEntity {

	

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "usuario_id", nullable = false, unique = false)
	private Usuario usuarioId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "role_id", nullable = false, unique = false)
	private Role roleId;

	public Usuario getUsuarioId() {
		return usuarioId;
	}

	public void setUsuarioId(Usuario usuarioId) {
		this.usuarioId = usuarioId;
	}

	public Role getRoleId() {
		return roleId;
	}

	public void setRoleId(Role roleId) {
		this.roleId = roleId;
	}

}
//IREPOSITORY USUARIOSROLES
package com.persona.Backend.IRepository.Security;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Security.UsuariosRoles;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IUsuariosRolesRepository extends IBaseRepository<UsuariosRoles, Long>{

}
//ISERVICE USUARIOSROLES
package com.persona.Backend.IService.Security;

import com.persona.Backend.Entity.Security.UsuariosRoles;
import com.persona.Backend.IService.IBaseService;

public interface IUsuariosRolesService extends IBaseService<UsuariosRoles> {

}
//SERVICE USUARIOSROLES
package com.persona.Backend.Service.Security;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Security.UsuariosRoles;
import com.persona.Backend.IService.Security.IUsuariosRolesService;
import com.persona.Backend.Service.BaseService;

@Service
public class UsuariosRolesService extends BaseService<UsuariosRoles> implements IUsuariosRolesService {

}
//CONTROLLER USUARIOSROLES
package com.persona.Backend.Controller.Security;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Security.UsuariosRoles;

@CrossOrigin("*")//permite que cualquier dominio tenga acceso a el
@RestController
@RequestMapping("/api/v1/base/security/usuarios_roles")
public class UsuariosRolesController extends BaseController<UsuariosRoles> {

}

```
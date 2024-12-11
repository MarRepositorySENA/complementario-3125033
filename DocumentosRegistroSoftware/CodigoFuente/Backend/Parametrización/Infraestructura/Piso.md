```
//ENTITY PISO 
package com.persona.Backend.Entity.Parameter.Infraestrutura;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "piso")
public class Piso extends BaseEntity {

	@Column(name = "codigo", length = 5, nullable = false)
	private String codigo;

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "sede_id", nullable = false, unique = false)
	private Sede sedeId;

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public Sede getSedeId() {
		return sedeId;
	}

	public void setSedeId(Sede sedeId) {
		this.sedeId = sedeId;
	}

}
//IREPOSITORY PISO
package com.persona.Backend.IRepository.Parameter.Infraestructura;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Piso;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IPisoRepository extends IBaseRepository<Piso, Long>{

}
//ISERVICE PISO
package com.persona.Backend.IService.Parameter.Infraestructura;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Piso;
import com.persona.Backend.IService.IBaseService;

public interface IPisoService extends IBaseService<Piso>{
	
	

}
//SERVICE PISO
package com.persona.Backend.Service.Parameter.Infraestructura;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Parameter.Infraestrutura.Piso;
import com.persona.Backend.IService.Parameter.Infraestructura.IPisoService;
import com.persona.Backend.Service.BaseService;

@Service
public class PisoService extends BaseService<Piso> implements IPisoService{

}
//CONTROLLER PISO
package com.persona.Backend.Controller.Parameter.Infraestructura;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Parameter.Infraestrutura.Piso;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/parameter/infraestructura/piso")
public class PisoController extends BaseController<Piso>{

}


```
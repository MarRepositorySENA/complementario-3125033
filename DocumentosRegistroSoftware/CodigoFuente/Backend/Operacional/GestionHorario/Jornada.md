
```
//ENTITY JORNADA
package com.persona.Backend.Entity.Operational.GestionHorario;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name="jornada")
public class Jornada extends BaseEntity{

	@Column(name = "codigo", length = 40, nullable = false)
	private String codigo;

	@Column(name = "nombre",  nullable = false)
	private String nombre;

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
	
	
}
//IREPOSITORY JORNADA
package com.persona.Backend.IRepository.Operational.GestionHorario;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionHorario.Jornada;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IJornadaRepository extends IBaseRepository<Jornada, Long>{

}
//ISERVICE JORNADA
package com.persona.Backend.IService.Operational.GestionHorario;

import com.persona.Backend.Entity.Operational.GestionHorario.Jornada;
import com.persona.Backend.IService.IBaseService;

public interface IJornadaService extends IBaseService<Jornada> {

}
//SERVICE JORNADA
package com.persona.Backend.Service.Operational.GestionHorario;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionHorario.Jornada;
import com.persona.Backend.IService.Operational.GestionHorario.IJornadaService;
import com.persona.Backend.Service.BaseService;

@Service
public class JornadaService extends BaseService<Jornada> implements IJornadaService{

}
//CONTROLLER JORNADA
package com.persona.Backend.Controller.Operational.GestionHorario;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionHorario.Jornada;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_horario/jornada")
public class JornadaController extends BaseController<Jornada>{

}


```